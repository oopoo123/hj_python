# 1. 홍길동의 중간고사 성적의 평균을 구하시오
# 80, 90, 70, 65, 100, 30, 50, 75
#
# 8개 과목의 중간고사 평균을 출력하시오
# * for문과 리스트를 이용하시오

list1 = [80, 90, 70, 65, 100, 30, 50, 75]

sm = len(list1)

sum = 0 # 초기값 없으면 에러

for score in list1:
    sum = sum + score #1)score=80, sum=0 2)score=90, sum=170 #)score=70, sum=240 ---
print(f"홍길동의 중간고사 평균은 {sum / sm}입니다")
print(f"홍길동의 중간고사 평균은 {sum / len(list1)}입니다")


# 2. 홍길동의 주민등록번호가 991201-1234567 이다
#
# 8번째 자리의 수가 1또는 3이면 남자 2 또는 4면 여자라고 할때
# 홍길동이 남자인지 여자인지 출력하는 프로그램을 작성하시오
# *for문 if문 사용, 논리연산 and or

jumin = ["991201-1234567"]

idx = 0

for i in jumin:
    if idx == 7:
        if i == "1" or i == "3":
            print("남자")
        elif i == "2" or i == "4":
            print("여자")
        else:
            print("오류")



# 3. 아래의 숫자들 중 짝수가 총 몇개인지 출력하는 프로그램을 작성하시오
#
# 5, 8, 17, 16, 20, 25, 41, 10, 9, 12, 14, 3, 6, 15
#
# *for문 if문 사용

numlist = [5, 8, 17, 16, 20, 25, 41, 10, 9, 12, 14, 3, 6, 15]

count = 0

for j in numlist:
    if j % 2 == 0:
        count = count + 1
        #count = count +1  count++ count--
        #count = count + 1 => count += 1

print(count)

# count 함수 활용법



# 4. 아래 모양으로 출력하는 프로그램을 작성하시오
#
# ***
# ***
# ***
# ***
# ***
#
# -단, print("*")를 이용하시오
#  print("***")사용 안됨 -> 이중 for문 사용

for k in range(5): # 0~4까지 총 5번 회전
    for l in range(3): # 0~2까지 총 3번 회전
        print("*", end = "")
    print("") # * 3개 붙여서 찍은 후 줄바꿈 (\n이 기본값)




# 5. 윤년은 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는 년도를 말한다
# 또는 년도가 400으로 나누어 떨어지면 윤년이다
# (예 : 2000년은 4롤 나누어 떨어지지만 100으로도 나누어 떨어지므로 윤년이 아니고, 2004년은 윤년이다)
#
# 1900년부터 2200년 사이에 윤년이 모두 몇년이 있는지를 출력하는 프로그램을 작성하시오
#
# -for, if, elif, and 사용

year = 2100

if year % 4 == 0 and year % 100 != 0:
    print(f"{year}년은 윤년입니다!")
elif year % 400 == 0:
    print(f"{year}년은 윤년입니다!")
else:
    print(f"{year}년은 평년입니다!")

print("----------------------------------------")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다!")
else:
    print(f"{year}년은 평년입니다!")

print("----------------------------------------")

countt = 0

for year in range(1900, 2201):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        countt = countt + 1

print(f"1900년 부터 2200년 사이의 윤년의 횟수는 총 {countt}번 입니다!")