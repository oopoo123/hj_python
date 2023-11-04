
a = [1, 2, 3]

print(id(a)) #id 변수나 리스트의 램의 주소를 알려주는 함수

b = a # b는 a의 주소만 복사하는 개념 리스트[1, 2, 3]이 또 복사를 한 개념이 아님
print(id(b)) # 얕은 복사

a[0] = 100

print(b)

a = [1, 2, 3]

b = a[0:]

print(id(a))
print(id(b)) # 깊은 복사

a1 = b1 = 10
print(id(a1))
print(id(b1))

a = 10
b = 20

temp = a
a = b
b = temp

a, b = b, a # a와 b의 값을 바꿈(파이썬만 가능)



