# map 함수 -> map(function, iterable)

def mul(a):
    return a * 10

print(list(map(mul, [1, 2, 3, 4])))

print(list(map(lambda a:a * 10, [1, 2, 3, 4])))

print("-----------------------------")

print(max(10, 20, 5)) # 최대값
print(min(10, 20, 5)) # 최소값

print("-----------------------------")

print(chr(65))
print(ord("A"))

print("-----------------------------")

print(pow(10, 2)) # 제곱함수 10의 2제곱

print(round(4.7)) # 반올림해서 정수로 변환
print(round(1.312567, 5)) # 소수점 5자리까지만 출력 -> 6자리에서 반올림

print("-----------------------------")

print(sorted([10, 5, 3, 20, 6, 7])) # 오름차순 정렬
print(sorted([10, 5, 3, 20, 6, 7], reverse=True)) # 내림차순 정렬

print("-----------------------------")

a = 123 # 숫자 -> 정수

b = str(a) # 숫자 -> 문자로 변환

print(sum([10, 20, 30]))

print(list("Korea"))
print(tuple("Korea"))

c = [1, 2, 3]

print(type(c)) # 자료의 종류(타입)




