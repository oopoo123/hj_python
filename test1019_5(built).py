
print(lambda a: a > 0, [1, -1, -2, 3, 0, 10])

print("-----------------------------")

print((lambda x, y : x + y)(10, 20))

print("-----------------------------")

ave = lambda a, b: (a + b) / 2

print(ave(10, 20))

print("-----------------------------")
def aver(a, b):
    return (a + b) / 2

print(aver(10, 20))

print("-----------------------------")

print(hex(100)) # 10진수를 16진수로 바꿔줌
print(bin(100)) # 10진수를 2진수로 바꿔줌
print(oct(100)) # 10진수를 8진수로 바꿔줌

