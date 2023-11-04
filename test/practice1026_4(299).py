#14

import operator

data = [
        ("윤서현", 15, 25),
        ("김예지", 13, 31),
        ("박예원", 15, 34),
        ("송순자", 15, 57),
        ("김시우", 15, 48)
]

print(sorted(data, key=operator.itemgetter(1))) #오름차순
print(sorted(data, key=operator.itemgetter(1), reverse=True))# 내림차순

#15
import itertools

students = ["홍길동", "이순신", "김유신", "강감찬"]

print(list(itertools.combinations(students, 2)))

#16
str = "abcd"

print(list(itertools.permutations(str, 4)))

#17

import random

list1 = ["김승현", "김진호", "강춘자", "이예준", "김현주"]
list2 = ["청소", "빨래", "설거지"]

list1 = random.sample(list1, 5) # 5명을 무작위 순서로 섞음

list3 = itertools.zip_longest(list1, list2, fillvalue="휴식")

for i in list3:
    print(i)


#18 (최대공약수 구하기)

import math

width = 200
height = 80

size1 = math.gcd(200, 80) # 정사각형 타일의 한변의 길이(최대공약수)

print(size1) # 40

numWidth = width / size1 # 가로로 들어갈 수 있는 타일의 수
numHeight = height / size1 # 세로로 들어갈 수 있는 타일의 수

print(int(numHeight * numWidth))

