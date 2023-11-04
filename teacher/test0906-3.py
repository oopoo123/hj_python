# 문자열 포매팅(formatting) : 문자열 안에 특정 값(숫자,문자열)을 삽입하는 방법

num = 10

print("I eat %d apples" % num) # 정수

str = "ten"

print("I eat %s apples" % str) # 문자열

numf = 10.7

print("I eat %0.1f apples" % numf) # 실수 - %0.1f 소수점 뒤에 나올 숫자의 개수