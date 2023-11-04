# 리스트 안의 모든 원소의 합을 구하시오

list1 = [70, 50, 90, 100, 120, 280]

sum = 0

for score in list1:
    sum = sum + score #누적식
    print(f"리스트의 모든 원소의 합은 {sum}입니다")
# 1회전=sum=70, 2회전=sum=120 위 리스트 원소 숫자만큼 계속 누적 합
# score에 list1의 원소가 누적 되는데 +라서 더해진다 누적 됨



