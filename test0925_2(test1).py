# 3의 배수의 합 구하기
# While 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자

result = 0
i = 1
while i <= 1000: # (3을 나누어 떨어지면 3의 배수)
    if i % 3 == 0: # result = result + i
        result += i # i = i + 1
    i += 1

print(result)