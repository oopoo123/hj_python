# continue(계속) 문

a = 0

while a < 10:
    a = a + 1
    if a % 2 == 0: # 해당 조건을 만족하는 a는 모두 짝수
        print(f"{a}는 짝수입니다")
        continue # 앞이 참이면 다시 첨으로 돌아가서 시작해라 뒷 문장은 실행 안됨
    print(f"{a}는 홀수입니다")

if a == 10: print("안녕!") #한줄 if문일 경우 바로 옆에 쓸때도 있다

