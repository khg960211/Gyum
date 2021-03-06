# -*- coding: utf-8 -*-
import os
import sys
import glob
from ctypes import windll, Structure, c_short, c_ushort, byref
from optparse import OptionParser
sys.path.insert(0, 'D:\\Gyum\Project\engine\kavcore')
import k2engine
import py_compile
import shutil

#-------------------------------------------------------------------------------
# 주요 상수
#-------------------------------------------------------------------------------
KAV_VERSION = '0.27'
KAV_BUILDDATE = 'Nov 21 2019'
KAV_LASTYEAR = KAV_BUILDDATE[len(KAV_BUILDDATE)-4:]

#-------------------------------------------------------------------------------
# 콘솔에 색깔 출력을 위한 클래스 및 함수들
#-------------------------------------------------------------------------------
FOREGROUND_BLACK = 0x0000
FOREGROUND_BLUE = 0x0001
FOREGROUNG_GREEN = 0x0002
FOREGROUND_CYAN = 0x0003
FOREGROUND_RED = 0x0004
FOREGROUND_MAGENTA = 0x0005
FOREGROUND_YELLOW = 0x0006
FOREGROUND_GREY = 0x0007
FOREGROUND_INTENSITY = 0x0008 # foreground color is intensifited.

BACKGROUND_BLACK = 0x0000
BACKGROUND_BLUE = 0x0010
BACKGROUND_GREEN = 0x0020
BACKGROUND_CYAN = 0x0030
BACKGROUND_RED = 0x0040
BACKGROUND_MAGENTA = 0x0050
BACKGROUND_YELLOW = 0x0060
BACKGROUND_GREY = 0x0070
BACKGROUND_INTENSITY = 0x0080 # background color is intensified.

SHORT = c_short
WORD = c_ushort

class Coord(Structure):
    _fields_ = [
    ("X", SHORT),
    ("Y", SHORT)]

class SmallRect(Structure):
    _fields_ = [
    ("Left", SHORT),
    ("Top", SHORT),
    ("Right", SHORT),
    ("Bottom", SHORT)]

class ConsoleScreenBufferInfo(Structure):
    _fields_ = [
    ("dwSize", Coord),
    ("dwCursorPosition", Coord),
    ("wAttributes", WORD),
    ("stWindow", SmallRect),
    ("dwMaximumWindowWize", Coord)]

# winbase.h
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

stdout_handle = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
GetConsoleScreenBufferInfo = windll.kernel32.GetConsoleScreenBufferInfo

def get_text_attr():
    csbi = ConsoleScreenBufferInfo()
    GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
    return csbi.wAttributes

def set_text_attr(color):
    SetConsoleTextAttribute(stdout_handle, color)

def cprint(msg, color):
    default_colors = get_text_attr()
    default_bg = default_colors & 0x00F0

    set_text_attr(color | default_bg)
    sys.stdout.write(msg)
    set_text_attr(default_colors)

    sys.stdout.flush()

def print_error(msg):
    cprint('Error: ', FOREGROUND_RED | FOREGROUND_INTENSITY)
    print (msg)

#-------------------------------------------------------------------------------
# print_k2logo()
# 백신 로고를 출력한다.
#-------------------------------------------------------------------------------
def print_k2logo():
    logo = '''KICOM Anti-Virus II (for %s) Ver %s (%s)
Copyright (C) 1995-%s Kei Choi. All rights reserved.
'''

    print '--------------------------------------------------------------------'
    s = logo % (sys.platform.upper(), KAV_VERSION, KAV_BUILDDATE, KAV_LASTYEAR)
    cprint(s, FOREGROUND_CYAN | FOREGROUND_INTENSITY)
    print '--------------------------------------------------------------------'

#-------------------------------------------------------------------------------
# 파이썬의 옵션 파서를 새롭게 정의한다.
# 에러문을 세세하게 조정할 수 있다.
#-------------------------------------------------------------------------------
class OptionPasringError(RuntimeError):
    def __init__(self, msg):
        self.msg = msg

class OptionParsingExit(Exception):
    def __init__(self, status, msg):
        self.msg= msg
        self.status = status

class ModifiedOptionParser(OptionParser):
    def error(self, msg):
        raise OptionPasringError(msg)

    def exit(self, status=0, msg=None):
        raise OptionParsingExit(status, msg)

#-------------------------------------------------------------------------------
# define_options()
# 백신의 옵션을 정의한다.
#-------------------------------------------------------------------------------
def define_options():
    usage = "Usage: %prog path[s] [options]"
    parser = ModifiedOptionParser(add_help_option=False, usage=usage)

    parser.add_option("-f", "--files", action="store_true", dest="opt_files", default=True)
    parser.add_option("-I", "--list", action="store_true", dest="opt_list", default=False)
    parser.add_option("-V", "--vlist", action="store_true", dest="opt_vlist", default=False)
    parser.add_option("-?", "--help", action="store_true", dest="opt_help", default=False)

    return parser

#-------------------------------------------------------------------------------
# parser_options()
# 백신의 옵션을 분석한다.
#-------------------------------------------------------------------------------
def parser_options():
    parser = define_options() # 백신 옵션 정의

    if len(sys.argv) < 2:
        return 'NONE_OPTION', None
    else:
        try:
            (options, args) = parser.parse_args()
            if len(args) == 0:
                return options, None
        except OptionPasringError, e: # 잘못된 옵션 사용일 경우
            return 'ILLEGAL_OPTION', e.msg
        except OptionParsingExit, e:
            return 'ILLEGAL_OPTION', e.msg

        return options, args

#-------------------------------------------------------------------------------
# print_usage()
# 백신의 사용법을 출력한다.
#-------------------------------------------------------------------------------
def print_usage():
    print '\nUsage: k2.py path[s] [options]'

#-------------------------------------------------------------------------------
# print_options()
# 백신의 옵션을 출력한다.
#-------------------------------------------------------------------------------
def print_options():
    options_string = \
        '''Options:
                -f,     --files         scan files *
                -I,     --list          display all files
                -V,     --vlist         display virus list
                -?,     --help          this help
                                        * = default option'''
    print options_string

#-------------------------------------------------------------------------------
# listvirus의 콜백 함수
#-------------------------------------------------------------------------------
def listvirus_callback(plugin_name, vnames):
    for vname in vnames:
        print '%-50s [%s.kmd]' % (vname, plugin_name)

#-------------------------------------------------------------------------------
# 악성코드 결과를 한 줄에 출력하기 위한 함수
#-------------------------------------------------------------------------------
def convert_display_filename(real_filename):
    # 출력용 이름
    fsencoding = sys.getfilesystemencoding() or sys.getdefaultencoding()
    display_filename = unicode(real_filename, fsencoding).encode(sys.stdout.encoding, 'replace')
    return display_filename

def display_line(filename, message, message_color):
    filename += ' '
    filename = convert_display_filename(filename)
    len_fname = len(filename)
    len_msg = len(message)

    if len_fname + 1 + len_msg < 79:
        fname = '%s' % filename
    else:
        able_size = 79 - len_msg
        able_size -= 5 # ...
        min_size = able_size / 2
        if able_size % 2 == 0:
            fname1 = filename[:min_size-1]
        else:
            fname1 = filename[:min_size]
        fname2 = filename[len_fname - min_size:]

        fname = '%s ... %s' % (fname1, fname2)

    cprint(fname + ' ', FOREGROUND_GREY)
    cprint(message + '\n', message_color)

#-------------------------------------------------------------------------------
# scan의 콜백 함수
#-------------------------------------------------------------------------------
def scan_callback(ret_value):
    real_name = ret_value['filename']

    disp_name = '%s' % real_name

    if ret_value['result']:
        state = 'infected'

        vname = ret_value['virus_name']
        message = '%s : %s' % (state, vname)
        message_color = FOREGROUND_RED | FOREGROUND_INTENSITY
    else:
        message = 'ok'
        message_color = FOREGROUND_GREY | FOREGROUND_INTENSITY

    display_line(disp_name, message, message_color)

#-------------------------------------------------------------------------------
# print_result(result)
# 악성코드 검사 결과를 출력한다.
# 입력값 : result - 악성코드 검사 결과
#-------------------------------------------------------------------------------
def print_result(result):
    print
    print

    cprint('Results:\n', FOREGROUND_GREY | FOREGROUND_INTENSITY)
    cprint('Folders           :%d\n' % result['Folders'], FOREGROUND_GREY | FOREGROUND_INTENSITY)
    cprint('Files             :%d\n' % result['Files'], FOREGROUND_GREY | FOREGROUND_INTENSITY)
    cprint('Infected_files    :%d\n' % result['Infected_files'], FOREGROUND_GREY | FOREGROUND_INTENSITY)
    cprint('Identified_viruses:%d\n' % result['Identified_viruses'], FOREGROUND_GREY | FOREGROUND_INTENSITY)
    cprint('I/O errors        :%d\n' % result['IO_errors'], FOREGROUND_GREY | FOREGROUND_INTENSITY)

    print

#-------------------------------------------------------------------------------
# main()
#-------------------------------------------------------------------------------
def main():
    # 옵션 분석
    options, args = parser_options()

    # 로고 출력
    print_k2logo()

    # 잘못된 옵션인가?
    if options == 'NONE_OPTION': # 옵션이 없는 경우
        print_usage()
        print_options()
        return 0
    elif options == 'ILLEGAL_OPTION': # 정의되지 않은 옵션을 사용한 경우
        print_usage()
        print 'Error: %s' % args # 에러 메시지가 담겨 있음
        return 0

    # help 옵션을 사용한 경우
    if options.opt_help:
        print_usage()
        print_options()
        return 0

    # 백신 엔진 구동
    k2 = k2engine.Engine(debug=False) # 엔진 클래스
    if not k2.set_plugins('plugins'): # 플러그인 엔진 설정
        print
        print_error('KICOM Anti-Virus Engine set_plugins')
        return 0

    kav = k2.create_instance()
    if not kav:
        print
        print_error('KICOM Anti-Virus Engine create_instance')
        return 0

    if not kav.init(): # 전체 플러그인 엔진 초기화
        print
        print_error('KICOM Anti-Virus Engine init')
        return 0

    # 엔진 버전을 출력
    c = kav.get_version()
    msg = '\rLast updated %s UTC\n\n' % c.ctime()
    cprint(msg, FOREGROUND_GREY)

    # 진단 / 치료 가능한 악성코드 수 출력
    msg = 'Signature number : %d\n\n' % kav.get_signum()
    cprint(msg, FOREGROUND_GREY)

    kav.set_options(options) # 옵션을 설정

    if options.opt_vlist is True: # 악성코드 목록 출력?
        kav.listvirus(listvirus_callback)
    else:
        if args:
            kav.set_result() # 악성코드 검사 결과를 초기화

            # 검사용 path (다중 경로 지원)
            for scan_path in args: # 옵션을 제외한 첫 번째가 검사 대상
                scan_path = os.path.abspath(scan_path)

                if os.path.exists(scan_path): # 폴더 혹은 파일이 존재하는가?
                    kav.scan(scan_path, scan_callback)
                else:
                    print_error('Invalid path: \'%s\'' % scan_path)

            # 악성코드 검사 결과 출력
            ret = kav.get_result()
            print_result(ret)

    kav.uninit()

if __name__ == '__main__':
    main()
