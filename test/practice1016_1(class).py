
# 1. Student 클래스를 만들고 생성자로 나이 (age), 학년(grade), 이름(name)을
# 입력 받아 초기화 하시오

class Student:
    def __init__(self, age, grade, name):
        self.age = age
        self.grade = grade
        self.name = name



# 2. 1번의 Student 클래스로 객체 (s1)를 선언한 후 이름(name)을 출력하시오

s1 = Student(25, 2, "홍길동")

print(s1.name)



# 3. 아래 코드가 출력결과와 같이 동작하도록 Car 클래스를 정의 하시오. (생성자 사용)

# car1 = Car(4, 1000)
# print(car1.바퀴)
# print(car1.가격)

# -----------------------
# <출력결과>
# 4
# 1000

class Car:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car1 = Car(4, 1000)
print(car1.바퀴)
print(car1.가격)

# 4.3번의 Car 클래스를 상속 받는 Bicycle 클래스를 만들고, 아래 처럼
# 구동계 정보까지 출력하는 클래스로 제작하시오
# bicycle1 = Bicycle(2, 100, "시마노")
# print(bicycle1.tire)
# print(bicycle1.price)
# print(bicycle1.drivertrain)
#
# ----------------------------
# <출력결과>
# 2
# 100
# 시마노

class Bicycle(Car):