s1 = set([1,2,3,4]) # set(집합) 선언

print(s1)

s2 = set("Korea")

print(s2) #{'K', 'r', 'o', 'a', 'e'} {'e', 'K', 'o', 'a', 'r'}

s3 = set([1,1,2,2,2,3,3,4,5])

print(s3) #{1, 2, 3, 4, 5}

# print(s1[0]) set구조는 인덱싱 불가

list1 = list(s1) #set을 list구조로 변환 후 인덱싱 해야함
print(list1[0])
tu1 = tuple(s1)
print(tu1[0]) #set을 tuple구조로 변환 후 인덱싱 해야함

set1 = set([1,2,3,4,5])
set2 = set([3,4,5,6,7])

print(set1|set2) #합집합
print(set1&set2) #교집합
print(set1-set2) #차집합

set3 = set([1,2,3])

set3.add(100) # 새로운 값을 추가

print(set3)

set3.remove(100) # 특정 값 제거

print(set3)

set3.update([4,5,6]) #한 번에 여러개의 원소(리스트)를 추가

print(set3)