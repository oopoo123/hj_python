def pri(name):
    print(f"{name}님 반갑습니다") #프린트가 함수에 저장 되기 때문에 print를 할 필요가 없음

pri("홍길동")

def pri2(abc):
    print(f"{abc}님 반갑습니다")

pri2("김유신")

pri("홍길동")
# 위에서 밑으로 읽으니까 함수를 선언을 먼저하고 호출을 해야한다
# 가독성을 위해 함수들은 될수 있으면 모아 놓자

def sum(a, b):
    sum = a + b
    #print(f"{sum}") # 이렇게 프린트를 넣으면 바로 출력 안하면 print를 해서 출력
    return sum

a = sum(10, 20) # 저장을 하고 퇴근하기 때문에 저장을 해야함
print(a)


# 인수 4개를 받아 평균을 반환하는 함수를 선언하시오.(함수의 이름은 aber)
# 함수를 선언 후 (10, 20, 30, 40)를 넣어 함수를 호출하시오

def aver(a, b, c, d):
    sum = a + b + c + d
    return sum / 4

num1 = aver(10, 20, 30, 40)

print(num1)
