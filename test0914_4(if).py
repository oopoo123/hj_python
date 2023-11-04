a = 100
money = False

if money:
    print("성공!!!")
    print("축하합니다!!!")
#     print("한칸더!") #에러가 생긴다
else:
    print("실패!!!")
    print("위로합니다!!!")
#파이썬에서는 들여쓰기로 묶어서 한블록으로 처리함

x = 10
y = 20

if x != y:  # != 같지 않다
    print("x와 y는 같다!")
else:
    print("x와 y는 같지 않다!")

###논리 연산자###
# or 은 두개의 조건중 하나만 참이면 참으로 출력 해준다
# and 는 두개의 조건중 둘다 참이어야지만 참을 출력
# not 은 무조건 바꿔버림(T -> F, F -> T)

x = 10
y = 20

if x >= 10 or y >= 50:
    print("성공!")
else:
    print("실패!")

if x >= 10 and y >= 50:
    print("성공!")
else:
    print("실패!")

if not x >= 100 and y >= 1: # not을 먼저 풀고 뒤에를 함 앞 은 T 뒤도 T 니까 T
    print("성공!")
else:
    print("실패!")


