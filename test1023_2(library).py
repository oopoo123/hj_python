
# A군과 B양이 2021년 12월 14일부터 만나기 시작했다면
# 2023년 4월 5일은 둘이 사귄지 며칠째 되는 날일까?

import datetime # 날짜와 관게된 표준라이브러리
import time # 시간관련 표준라이브러리
#import glob # 사용하지 않는 라이브러리는 주석처리 또는 삭제

day1 = datetime.date(2021, 12, 14) # 2021-12-14 날짜타입으로 변환
day2 = datetime.date(2023, 4, 5)

dday = day2 - day1

print(dday)
print(dday.days)

print(day1.weekday()) # 0->월, 1->화, 2->수....2021년 12월 14일은 화요일
print(day1.isoweekday()) # 1->월, 2->화, 3->수

print(time.time()) # 현재시간-1970년 1월 1일 0시 0분 0초를 기준으로해서 현재시간까지의 초

print(time.localtime(time.time())) # 현재시간을 초로 년, 월, 일, 시, 분, 초..로 변환

print(time.ctime()) # 항상 현재시간만을 변환

print(time.strftime("%x", time.localtime(time.time())))
print(time.strftime("%c", time.localtime(time.time())))

# time.sleep()  ()안에 넣어지는 초만큼 프로그램을 일시정지할때 사용

for i in range(1, 1001):
    print(i)
    time.sleep(1.5)
    # time.sleep(x) x초만큼 프로그램을 일시정지하여 반복문내에서 타이머 역할을 함


print("-----------------------------")

day3 = datetime.date(2009, 11, 18) # 2009-11-18 날짜타입으로 변환
day4 = datetime.date(2023, 10, 23)

dday2 = day4 - day3

print(dday2.days)

print("-----------------------------")



