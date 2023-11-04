#11

import time

#2023/10/26 10:40:31
print(time.strftime("%Y/%m/%d %h:%M:%S"))

#13

import datetime

sister = datetime.date(1995, 11, 20)
brother = datetime.date(1998, 10, 6)

dayValue = brother - sister
print(dayValue.days) # 날짜만 출력 가능

