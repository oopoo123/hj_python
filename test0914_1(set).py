s1 = set([1, 2, 3, 4]) # set(집합) 선언

print(s1)

s2 = set("Korea")

print(s2) # 문자열은 원소를 하나씩 랜덤으로 출력

s3 = set([1, 1, 2, 2, 2, 3, 3, 4, 5])

print(s3) #같은 항목 제거 숫자는 sort는 해줌 오름차순

# print(s[0])
# print(s[0]) set 구조는 인덱싱 불가

list = list(s1) #set을 list구조로 변환 후 인덱싱 해야함
print(list[0])
tu1 = tuple(s1)
print(tu1[0])   #set 을 tuble구조로 변환 후 인덱싱 해야함
                #순서가 중요하지 않다

set1 = set([1, 2, 3, 4, 5])
set2 = set([3, 4, 5, 6, 7])

print(set1 | set2) #합집합
print(set1 & set2) #교집합
print(set1 - set2) #차집합

set3 = set([1, 2, 3])

set3.add(100)         # 새로운 값을 추가

print(set3)

set3.remove(100)      # 특정 값 제거

print(set3)

set3.update([4, 5, 6]) #한번에 여러개의 원소(리스트)를 추가

print(set3)



