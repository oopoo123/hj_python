
a = -100

b = abs(a) # 절대값 내장함수

print(b)

print("-----------------------------")

ch = 65 # 아스키코드 값
ch2 = 44032 # 유니코드 값 한글가능

print(chr(ch)) # 아스키코드 값을 입력하면 해당 코드의 문자가 반환

print(chr(ch2)) # 유니코드 값을 입력하면 해당 코드의 문자가 반환

print("-----------------------------")

list1 = [1, 2, 3]

print(dir(list1)) # 리스트 자료구조에서 사용할 수 있는 함수들의 목록이 반환됨

print(divmod(10, 3)) # 몫은 3 나머지는 1이 튜플 자료구조로 반환됨
print(10//3) # 몫 연산
print(10%3)  # 나머지 연산

print("-----------------------------")

# enumerate() 인덱스를 구할수 있다

for i, j in enumerate(["kor", "jap", "usa"]):
    # 순서가 있는 객체의 인덱스 값을 포함하는 enumerate 객체를 반환함
    print(i)
    print(j)

print("-----------------------------")

print("1 + 2")
print(eval("1 + 2")) # eval 문자열로 표현된 계산식을 계산한 결과값을 반환함
print(eval("'일'+'2'"))

print("-----------------------------")

