
#예외 처리
#1
print("프로그램을 시작합니다!")
b = 0
try:
    a = 10 / b # 에러 발생 가능성이 있는 라인
    print(a)
except:
    print("0 나누기 에러 발생!")


print("프로그램을 종료합니다!")

print("-----------------------------")

#2
print("프로그램을 시작합니다!")
b = 0
try:
    a = 10 / b # 에러 발생 가능성이 있는 라인
    print(a)
    print("1")
    print("2")
    print("3")
    print("4")

except:
    b = 1
    a = 10 / b
    print(a)
    print("0 나누기 에러 발생")

print("프로그램을 종료합니다!")

print("-----------------------------")

#3
print("프로그램을 시작합니다!")
b = 10
list1 = [1, 2, 3]
try:
    a = 10 / b # 에러 발생 가능성이 있는 라인
    print(list1[10])

except (ZeroDivisionError, IndexError) as e:
    b = 1
    a = 10 / b
    print(a)
    print(e)

print("프로그램을 종료합니다!")

print("-----------------------------")

#4
print("프로그램을 시작합니다!")
b = 10
list1 = [1, 2, 3]
try:
    a = 10 / b # 에러 발생 가능성이 있는 라인
    print(list1[10])

except Exception as e: # Exception 다른 에러들을 다 포괄 부모
    b = 1
    a = 10 / b
    print(a)
    print(e)
finally:
    print("finally에 들어가는 명령문은 무조건 실행")
    c = 100

print("프로그램을 종료합니다!")
