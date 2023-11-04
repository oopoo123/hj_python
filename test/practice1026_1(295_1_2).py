class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value = self.value + val # self.value += val


#이 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자.
#다음과 같이 동작하는 클래스를 만들어야 한다

class UpgradeCalculator(Calculator):
    def minus(self, num):
        self.value = self.value - num # val도 됨

cal = UpgradeCalculator() # 객체선언
cal.add(10) # 0 + 10
cal.minus(7) # 10 - 7

print(cal.value)

# 객체변수 value가 100 이상의 값은 가질 수 없도록 제한하는
# MaxLimitCalculator 클래스를 만들어 보자
# 즉 다음과 같이 동작해야한다
class MaxLimitCalculator(Calculator):
    def add(self, val):               ### 오버라이딩 ### 부모꺼 그냥 가져다 쓰는거
        self.value = self.value + val
        if self.value > 100:
            self.value = 100


cal2 = MaxLimitCalculator()
cal2.add(50) #value=0 -> value=50
cal2.add(60) #value=50 -> value=110 -> value=100

print(cal2.value)

#단 반드시 다음과 같은 Calculator 클래스를 상속해서 만들어야 한다.



