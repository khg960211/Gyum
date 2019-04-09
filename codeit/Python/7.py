# -*- coding: utf-8 -*- 
# Optional Parameters
# 파라미터의 기본값을 설저해두면 함수 호출을 할 때 파라미터에 해당되는 값을 넘겨주지 않았을 경우, 그 파라미터는 기본값을 가지게 된다.
# 이런 파라미터를 optional Parameters라고 부른다.
# 순서를 마지막에 써주어야 하며, 여러개를 정할 수 있다.

def myself(name, age, nationality = "한국", season = "여름", sports = "축구"):
    print("내 이름은 %s" % name)
    print("나이는 %d살" % age)
    print("국적은 %s" % nationality)
    print("좋아하는 계절은 %s" % season)
    print("좋아하는 스포츠는 %s" % sports)

myself("코드잇", 1)            # 기본값이 설정된 파라미터를 바꾸지 않을 때
print("----------------")
myself("코드잇", 1, "미국")     # 기본값이 설정된 파라미터를 바꾸었을 때
print("----------------")
myself("코드잇", 1, "미국", "겨울")     # 기본값이 설정된 파라미터를 바꾸었을 때
