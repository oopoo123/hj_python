
a = 1 # 전역변수 (전국구 얘는 함수 안에까지 영향을 미침 단 지역변수는 함수 밖으로 나올 수 없다)
b = 50

def scopeTest():
    a = 100
    b = 1000
    print(a) #함수 안 a를 출력, 지역변수
    print(b) #함수 안 b를 출력, 지역변수
    # 위의 a=1과 밑의 a=100이랑은 다르다 a=100은 함수 안에서의 a이다
    # a, b 즉 함수 안의 변수는 지역변수라고 한다

def scopeTest2():
    print(a) # 전역변수 a의 값

scopeTest()

scopeTest2()


print(a)
print(b)
