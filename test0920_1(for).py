list1 = [1, 2, 3, 4, 5]
# for i in list1:

# for문의 기본 구조
for i in [10, 40, 30, 100]:
    print(f"{i} 출력")


num = 0 # num 초기값이 0

for i in list1:
    num = num + 1  # num = 1, 2, 3, 4
    if i % 20  == 0:
        continue
    print(f"{num} 번째 회전")

print(f"위의 for문은 {num}번 반복하였습니다")

for i in list1:
    if i % 2  == 0:
        continue
    num = num + 1
    print(f"{num} 번째 회전")

print(f"위의 for문은 {num}번 반복하였습니다")

n = 0

for j in list1:
    print(f"{list1[n]}")
    n = n + 1


