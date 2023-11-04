
# 3. 1부터 입력 받은 임의의 정수까지의 모든 숫자의 곱을 반환하는 함수 mulFunc
# 를 작성하시오. (팩토리얼 함수 만들기-for, range 함수 이용)
#
# mulFunc(3)
# -> 3*2*1 -> 6을 반환하는 함수 제작

def mulFunc(num):
    sum = 1
    for i in range(1, num+1):
        sum = sum * i
    return sum


area = mulFunc(3)
print(area)

