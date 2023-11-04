a = "Korea Love" #10개의 인덱스 0~9까지 생성
#문자열 인덱싱(띄어쓰기도 1개의 인덱스)
print(a[6]) #L이 출력
print(a[-4]) #L이 출력 뒤에서부터

print(a[2:5]) #슬라이싱 인덱스에서 (끝번호는 출력이 안됨 +1해야 됨)
print(a[6:]) #2번째 인덱스 번호를 생략하면 마지막 번호를 뜻함
print(a[:4]) #1번째 인덱스 번호를 생략하면 첫번째 0부터의 번호를 뜻함

print(a[0:3],a[7:])

# 문자열 포매팅(formatting):문자열 안에 특정 값(숫자, 문자열)을 삽입하는 방법
num = 10
print("I eat %d apples" % num) #정수

str= "ten"
print("I eat %s apples" % str) #문자열

numf = 10.7

print("I eat %f apples" % numf) #실수 소수점 자리 기본 6자리까지 찍힘

print("I eat %0.1f apples" % numf) #실수-%0.1f 소수점 뒤에 나올 숫자의 개수

#format 함수를 활용한 포매팅 이방법을 더 많이 쓴다

num = 10
print("I eat {0} apples".format(num)) #식을 왜울 필요 없음

num2 = "ten"

print("I eat {0} apples {1}".format(num, num2))
print("I eat {1} apples {0}".format(num, num2))
#{0},{1}이건 인덱스가 num->{0}, num2->{1}


## f string(문자열) 포매팅 제일 많이 씀

print(f'I eat {num} apples {num2}') #직관적이고 가독성이 띄어남 ",'상관없음

print(f'I eat {num+1} apples {num2}') #{} 안에서는 변수간의 계산도 가능

num3 = 10.123456

print(f"내가 좋아하는 숫자는 {num3:0.2f} 입니다") #소수점 자리 지정
#f는 실수의 false 약자

num4 = 1.2346

print(f"숫자 : {num4:.3f}") # {num4 : 여기서 0.의 0은 생략 가능)
#기본적으로 반올림으로 끝자리는 된다

str = ("오늘 안녕하세요?")

print(f"저는 {str[3:5]} 합니다!") #f 문자열의 {}안에서는 index 사용 가능
# print(f"저는 {{str[3:5]}} 합니다!") #{} 넣고 싶을때






