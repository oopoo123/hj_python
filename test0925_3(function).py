def sum(x, y): # sum은 내가 작명 x, y 는 매개변수를 선언한다
    sum = x + y
    return sum # 반환한다 sum을


# def는 사용자정의함수 끝에는 return

print(sum(3, 4)) # 함수를 호출한다

#기본적인 함수 선언 함수 호출
def add(a, b):
    result = a + b
    return result

print(add(5, 7))


number1 = sum(5, 10) # sum 함수의 반환값(리턴값)을 number1 변수에 저장

def add(a, b): #<- a, b는 매개변수=함수에 입력으로 전달된 값을 받는 변수
    return a + b

print(add(5,4)) #<-3, 4는 인수=함수를 호출할 때 전달받는 입력값


#리턴값과 매개변수가 없는 경우
def pri():
    print("안녕")

pri()


def minus(a, b):      # 함수를 선언했다 a, b 매개변수(parameter)
    return  a - b

c = minus(10, 5) # 함수를 호출했다 10, 5 인수(arqument)
#minus 함수의 리턴값이 c에 저장
print(c)

# sum(100, "korea") # 매개변수 데이터 형식에 맞지 않는 인수가 함수 호출시에 입력되면 에러!