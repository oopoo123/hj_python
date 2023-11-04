
a = 10

b = 0


# if b == 0:
#     print("모든수는 0으로 나눌수 없습니다!!다시확인하세요!!")
# else:
#     print(a / b)


# try-except문-예외처리문(에러 예비책)

list1 = [1, 2, 3]

try:
    #print(list1[10])
    print(a / b) # 에러가 발생할 가능성이 있는 문장
    print(b / a)
except ZeroDivisionError as e:
    print("에러발생!!")
    print(e)
    #pass도 가능
    #ZeroDivisionError as e 생략 가능(어떤 에러인지 표시 안할꺼면)

print("안녕하세요") #예외처리가 되면 찍힘

print("----------------------------------------")

try:
    print(list1[10])
except:
    pass

print("안녕하세요") #예외처리가 되면 찍힘

print("----------------------------------------")

try:
    #print(a / b)  # 에러가 발생할 가능성이 있는 문장
    print(list1[10])
except Exception as e: # Exception 모든 에러 담당 클래스
    print(e)
    pass
finally:
    print("저는 무조건 실행되는 문장입니다 finally")

print("안녕하세요")