###리스트 컴프리헨션 사용하기
### 다음 소스 코드는 리스트의 요소 중에서 홀수만 골라 2를 곱한 값을 result 리스트에 담는 예제이다

numbers = [1, 2, 3, 4, 5]
result = []
for n in  numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)
###이 코드를 리스트 컴프리헨션을 사용하여 표현해 보자

numbers1 = [1, 2, 3, 4, 5]
result1 = [n * 2 for n in numbers1 if n % 2 == 1]

print(result1)
