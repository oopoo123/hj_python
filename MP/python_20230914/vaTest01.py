
a = [1,2,3]

print(id(a))

b = a
print(id(b))

a[0] = 100

print(b)

a = [1,2,3]

b = a[0:]

print(id(a))
print(id(b))

a1 = b1 = 10

print(id(a1))
print(id(b1))

a = 10
b = 20

temp = a
a = b
b = temp

a, b = b, a # a와 b의 값을 바꿈(파이썬만 가능)


