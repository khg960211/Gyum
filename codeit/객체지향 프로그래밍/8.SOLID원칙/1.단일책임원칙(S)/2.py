# -*- coding: utf-8 -*-
class StudentProfile:
    """학생 기본 정보 클래스"""
    def __init__(self, name, id, class_year):
        self.name = name
        self.id = id
        self.class_year = class_year

    def change_info(self, new_name, new_id, new_class_year):
        """학생 기본 정보 수정 메소드"""
        self.name = new_name
        self.id = new_id
        self.class_year = new_class_year


class GPAManager:
    """학생 학점 관리 클래스"""
    def __init__(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        """학점 추가 메소드"""
        if 0 <= grade <= 4.3:
            self.grades.append(grade)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산"""
        return sum(self.grades) / len(self.grades)


class ReportCardPrinter:
    """성적표 출력 클래스"""
    def __init__(self, student_profile, gpa_manager):
        self.student_profile = student_profile
        self.gpa_manager = gpa_manager

    def print(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n학번:{}\n평균 학점:{}"\
        .format(self.student_profile.name, self.student_profile.id,\
                self.student_profile.class_year, self.gpa_manager.get_average_gpa()))


class Student:
    """코드잇 대학생을 나타내는 클래스"""
    def __init__(self, name, id, class_year):
        self.profile = StudentProfile(name, id, class_year)
        self.grades = []
        self.gpa_manager = GPAManager(self.grades)
        self.report_card_printer = ReportCardPrinter(self.profile, self.gpa_manager)


# 학생 인스턴스 정의
younghoon = Student("강영훈", 12345678, 2016)
younghoon.profile.change_info("강영훈", 12345678, 2015)

# 학생 성적 추가
younghoon.gpa_manager.add_grade(3.0)
younghoon.gpa_manager.add_grade(3.33)
younghoon.gpa_manager.add_grade(3.67)
younghoon.gpa_manager.add_grade(4.3)

# 학생 성적표
younghoon.report_card_printer.print()
