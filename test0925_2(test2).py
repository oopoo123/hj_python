## 평균 점수 구하기
## A학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다
## [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
## for문을 사용하여 A학급의 평균 점수를 구해 보자

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0

for score in A:
    total += score

average = total / len(A) # len() list의 길이 (원소의 수)를 출력해주는 함수

print(average)