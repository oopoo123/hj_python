
import math # 수학 수식관련 라이브러리
import random

print(math.gcd(10, 20, 100)) # 최대공약수
print(math.lcm(10, 20, 100)) # 최소공배수

print("-----------------------------")

print(random.random()) # 0.0 ~ 1.0 사이의 실수 중에서 임의의 값 반환

print(int(random.random() * 10))

print("-----------------------------")

print(((int(random.random() * 10) % 6)) + 1) # 1~6사이의 임의 정수값을 출력
print(random.randint(1, 6)) # 1~6사이의 정수 중 임의의 정수값을 출력

print(random.choice([10, 2, 3, 4, 7])) # 입력된 리스트 중에 하나를 랜덤으로 반환

print(random.choice(["가위", "바위", "보"]))

data = random.sample([1, 2, 3, 4, 5], 3)
# 입력된 리스트에서 ,k값 수 만큼 랜덤으로 섞여진 리스트를 출력
print(data)