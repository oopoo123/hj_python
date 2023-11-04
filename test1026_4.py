
# int a = 10 (자바)
# a = "korea" -> error

a = 10
a= "korea"
#파이썬은 동적 프로그램 정수에서 문자열로 자동으로 알아서 변경
#자바는 안됨 정적 언어임
# 동적 프로그램 장점 쉽고 유연한 코딩 가능
# 단점 버그 발생할수 있음 어노테이션으로 단점 극복

b: int = 10 #(파이썬 타입 어노테이션) # mypy설치(에러 확인 패키지)

b = "korea"

def sum(a: int, b: int)->int:
    return a + b

result = sum(10, 20)


