# -*- coding: utf-8 -*- 
# 문자열 포맷팅 연습
wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (5, wage * 5, "달러"))
# 코드를 입력하세요.

# "1시간에 5710.8원 벌었습니다." 출력
print("%d시간에 %.1f%s 벌었습니다." % (1, wage * 1 * exchange_rate, "원"))
# 코드를 입력하세요.

# "5시간에 28554.0원 벌었습니다." 출력
print("%d시간에 %.1f%s 벌었습니다." % (5, wage * 5 * exchange_rate, "원"))
# 코드를 입력하세요.
