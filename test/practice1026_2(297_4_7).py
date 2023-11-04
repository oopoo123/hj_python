#4

print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))

def plusNum(x):
    return x > 0

#5

h1 = hex(234) # 16진수 0xea

print(h1)

print(int(h1, 16)) #16진수를 10진수로

#6

print(list(map(lambda x : x * 3, [1, 2, 3, 4])))

#7

list1 = [-8, 2, 7, 5, -3, 5, 0, 1]

print(max(list1)+min(list1))

