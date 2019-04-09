# -*- coding: utf-8 -*-
# 주민등록번호 YYMMDD-abcdefg는 총 13자리로, 앞의 6자리(YYMMDD)는 생년월일을 의미합니다.
# 뒤의 7자리 abcdefg 중 맨 앞자리 a는 성별을 의미하고,
# 두번째와 세번째 자리 bc는 출생등록지에 해당하는 지방자치단체의 고유번호입니다.
# 즉 여러분이 언제, 어디서 태어났는지와 성별만 안다면,
# 마지막 4개의 숫자 defg를 제외한 앞의 9개 숫자는 쉽게 알 수 있다는 것입니다.
# 이러한 의미에서, 저희는 주민등록번호의 마지막 4개의 숫자 defg를 가려주는 보안 프로그램을 만들어보려고 합니다.
# 문자열 security_number를 파라미터로 받고, security_number의 마지막 네 글자를 '*'로 가린
# 문자열 값을 리턴해주는 함수 mask_security_number를 쓰세요. 주민등록번호 가운데에 구분해주는 '-' 작대기 기호가 있든 없든,
# 아래와 같이 마지막 네 글자가 '*'로 가려져야 합니다.
def mask_security_number(security_number):
    # 코드를 입력하세요.
    return security_number[:len(security_number) - 4] + "****"

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
