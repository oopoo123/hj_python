# 다음 리스트의 원소(숫자) 중 소수만을 가진 리스트로 출력하는
# 프로그램을 작성하시오
# listNum = [10, 20, 5, 3, 4, 7, 11]
# 출력 listPN = [5, 3, 7, 11]


listNum = [10, 20, 5, 3, 4, 7, 11]

listPN = []

for i in listNum:
    count = 0
    for j in range(2, i): # j -> 2~9
        if i % j == 0:
            count = 1     # 플래그값 신호를 나타내는
    if count == 0:
        listPN.append(i)

print(listPN)


## 컴프레션
result = [x*y for x in range(2, 10)
              for y in range(1, 10)]

print(result)


