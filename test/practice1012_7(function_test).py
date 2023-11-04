
# 팩토리얼 함수 -> 재귀함수(본인 함수 안에 호출)

def factorialFunc(num):
    if(num > 1):
        return num * factorialFunc(num - 1)
    else:
        return 1

print(factorialFunc(4))