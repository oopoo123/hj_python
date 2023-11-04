
# 6. 1~365 까지의 모든 숫자의 합을 출력하는 프로그램을 작성하시오

sum = 0 # 초기값

for i in range(1, 366):
    sum = sum + i

print(sum)

## sum = sum + i (누적식) 외우자!!!
