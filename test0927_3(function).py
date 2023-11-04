#[] 리스트, {} , ()튜플
def mulSum(a, b):
    sum = a + b
    mul = a * b
    divid = a / b
    return sum, mul, divid # 다른언어는 리턴값이 무조건 하나이지만 파이썬은 다중 가능

result = mulSum(3,2)

result1, result2, result3 = mulSum(10,2)

print(result)

print(result1, result2, result3)
