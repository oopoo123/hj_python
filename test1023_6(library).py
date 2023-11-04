# functools
import functools

# operator
import operator

list1 = [1, 2, 3, 4, 5]

result = functools.reduce(lambda x, y : x + y, list1) # list1의 모든 원소의 누적합

print(result)

students =[("홍길동", 21, "A"), ("김유신", 34, "B"), ("이순신", 27, "O")]

print(sorted((students))) # 무조건 첫번째 원소의 오름차순 정렬
print(sorted(students, key=operator.itemgetter(1)))
 # 원하는 기준으로 정렬 -> sorted key값을 원하는 기준의 인덱스로 설정

students2 = [
    {"name" : "홍길동", "age" : "21", "blood" : "A"},
    {"name" : "김유신", "age" : "34", "blood" : "B"},
    {"name" : "이순신", "age" : "27", "blood" : "O"}
]

print(sorted(students2, key=operator.itemgetter("age")))
