
# 1. 가격을 입력 받으면 20% 할인된 가격을 반환하는 함수 saleFunc를 작성하시오
#
# 실행 예)
# saleFunc(1000)
# -> 800을 반환하는 함수 제작

def saleFunc(sale):
    price = sale * 0.8
    return price


area = saleFunc(1000)
print(area)

# 2. 연봉을 입력 받으면 연봉을 12개월로 나눈 월급을 반환하는 salaryFunc
# 함수를 작성하시오 (단, 월급의 소수점(1원미만)은 버림하여 반환하시오)
#
# 실행 예)
# salaryFunc(12000000)
# -> 1000000 반환하는 함수 제작

def salaryFunc(salary):
    price2 = salary / 12 # 나눗셈을 하면 결과가 실수로 변경
    price2 = int(price2) # 정수로 변환하면서 소수점 자리는 다 버림
    return price2

area2 = salaryFunc(12000000)
print(area2)

