
a = [1, 2, 3] # 반복가능한 객체
b = (1, 2, 3) # 반복가능한 객체(튜플)

for i in a:
    print(i)

ia = iter(a) # 이터레이터

print(ia)

print(next(ia)) # 예를들어 화살표가 각 인덱스 앞에 화살표가 가르키고 있는데 next가 한칸씩 이동 시킴 3이후론 4가 없으므로 안나옴
print(next(ia))
print(next(ia))
# print(next(ia))

# for j in ia:
#     print(j)
# for j in ia:
#     print(j)

#while next(레코드) 이런식으로 사용 레코드를 가져 와서 개수 확인 할때