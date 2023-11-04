# 리스트 자료형 연습

#띄어쓰기를 추천한다 이유는 가독성
a = [] # 리스트 선언
b = [1, 2, 3]
c = ["kor", "jpa", "chn"]
d = [1, 2, "kor", "jpa", 1.9] # 리스트는 섞어서 저장할수 있다

print(b)
print(b[0])
print(d)

print(b[0] + b[2])

e = [1, 2, ["kor", "jpa"]]
print(e[1])
print(e[2])  #['kor', 'jpa']
print(e[2][0]) #kor만 뽑아서 나옴

f = [1, 2, 3, 4, 5]

print(f[1:2]) # [2] -> 원소가 하나인 리스트
print(f[1])  # 2 -> 정수로 사용