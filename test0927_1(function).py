# 함수 이름은 첫글자는 왠만하면 소문자로 대문자도 에러는 안나지만 다른 함수쓸때 대문자 쓰는 경우가 있어서 헷갈림
# 함수 이름에 -(하이픈)은 쓸수는 있지만 왠만하면 _(언더스코어)를 쓰는것이 좋다 보통 띄어쓰기에 쓰임
# 함수 이름, 매개 변수 이름을 잘 정해야지 헷갈리지 않는다
# 만들 함수는 항상 위에 모아서 만들어 놓는게 좋다

def change_rate(won, rate): # won, rate = 매개변수
    dollar = won / rate

    return dollar
# 함수 선언

def prName(): # 매개변수와 리턴값이 없는 함수
    print("홍길동")

def prAge(): # 매개변수가 없는 함수
    age = 27
    return age # 리턴값을 돌려 줌

def prGrade(grade): # 리턴 값이 없는 함수
    print(f"{grade * 3}학년 입니다!") # 프린터를 찍고 끝

dollar1 = change_rate(100000, 1350)
# 함수 호출

print(dollar1)
# 함수 출력

prName()

age = prAge()

print(age)

grade = prGrade(3)



