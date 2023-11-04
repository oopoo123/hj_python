# 리스트 자료형 연습

a = [] # 리스트 선언
b = [1, 2, 3]
c = ["kor", "jpa", "chn"]
d = [1, 2, "kor", "jpa", 1.9]

print(b)
print(b[0])
print(d)

e = [1, 2, ["kor", "jpa"]]
print(e)
print(e[1])
print(e[2])
print(e[2][0]) #['kor', 'jpa']

f = [1,2,3,4,5]

print(f[1:2]) # [2] -> 원소가 하나인 리스트
print(f[1]) # 2 -> 정수로 사용