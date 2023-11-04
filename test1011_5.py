# Calulator 클래스로 cal이라는 객체를 선언하고,
# cal 객체를 이용하여 10과 20의 사칙연산 결과를 출력하시오
# 단, 초기화자를 추가하여 객체가 선언될 때 10과 20으로
# 객체변수를 초기화하여 출력하시오

class Calculator:

    def __init__(self, a, b):
        self.x = a # 객체변수 초기화
        self.y = b

    def add(self):
        result = self.x + self.y
        return result

    def minus(self):
        result = self.x - self.y
        return result

    def mul(self):
        result = self.x * self.y
        return result

    def divid(self):
        result = self.x / self.y
        return result

cal = Calculator(10, 20)

result1 = cal.add()
result2 = cal.minus()
result3 = cal.mul()
result4 = cal.divid()

print(result1)
print(result2)
print(result3)
print(result4)
print(f"더하면 {result1} 입니다")
print(f"빼면 {result2} 입니다")
print(f"곱하면 {result3} 입니다")
print(f"나누면 {result4} 입니다")