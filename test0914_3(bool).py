bool1 = True # 불타입(boolean type)

bool2 = 100 > 10

print(bool2)

a = 100
b = "korea"
c = 10.88

print(type(a))
print(type(b))
print(type(c))
print(type(bool1))

str1 = "" # 빈 자료형은 거짓으로 판단한다 / 0 = 거짓, 1 = 참(0을 제외한 모든수는 참 -도 참이다)

print(bool("jao"))
print(bool(""))
print(bool([100]))

print(bool(0)) # 0을 제외한 모든 숫자는 True
print(bool(-1000))
print(bool(None))



