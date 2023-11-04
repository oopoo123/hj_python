# 1. 3개의 정수값을 입력 받아 짝수인지 홀수인지 판별하여 출력하는 함수를 작성하시오
# 함수의 이름은 evenOrOdd로 작성
#
# 예) evenOrOdd(3, 10, 50)
# 3은 홀수입니다
# 10은 짝수입니다
# 50은 짝수입니다

#1
def evenOrOdd(a, b, c):
    if a % 2 == 0:
        print(f"{a}은 짝수입니다")
    else:
        print(f"{a} 홀수입니다")
    if b % 2 == 0:
        print(f"{b}은 짝수입니다")
    else:
        print(f"{b} 홀수입니다")
    if c % 2 == 0:
        print(f"{c}은 짝수입니다")
    else:
        print(f"{c} 홀수입니다")


evenOrOdd(3, 10, 50)

#2
def listOdd(a, b, c):
    list1 = [a, b, c]
    for i in list1:
        if i % 2 == 0:
            print(f"{i}는 짝수입니다")
        else:
            print(f"{i}는 홀수입니다")

listOdd(3, 10, 50)