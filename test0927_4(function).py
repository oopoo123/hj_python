
def printName(name, age, studentYes = 1): # 매개변수가 초기값 미리 설정하기
    print(name)
    print(age)
    if studentYes == 1:
        print("학생")
    else:
        print("직장인")

printName("홍길동", 27, 1)
printName("홍길동", 27, 0)

printName("김유신", 31)
#studentYes의 초기값이 1로 설정되어 있으므로 함수 호출시 studentYes 인수 생략 가능
