# 1부터 100까지 합을 구하시오!

sum = 0

for i in range(1, 101):
    sum = sum + i  # 누적값

print(sum)

# 구구단 2단 결과 출력

for j in range(1, 10):
    print(2 * j)

print("------------------------------------------------")

##### 2단~9단 구구단 결과 출력(2중 for문) #####

for k in range(2, 10):
    print(f"---------{k} 단 출력-----------")
    for l in range(1, 10):
        # print(k * l)
        print(f"{k} x {l} = {k * l}")
    print("----------------------------") #들여쓰기 위치 확인

# 첫 회전 k 2가 고정되고 밑에 l이 1에서 9까지 한바퀴 돌고 다시 위가 k가 3이 되고 반복
# k안에 l이 있으므로 k원소 하나 실행되면 l원소들이 한바퀴 돈다

print("------------------------------------------------")

for a in range(1, 6):
    print("안녕하세요!!!\n") #\n 기본값으로 안보이지만 삽입되어 있다 하나더 넣어서 두줄

for a in range(1, 6):
    print("안녕하세요!!!", end= " / ") # end를 치면 줄바꿈 해제 역슬래쉬가 없어짐 공백도 가능

for k in range(2, 10):
    print(f"---------{k} 단 출력-----------")
    for l in range(1, 10):
        # print(k * l)
        print(f"{k} x {l} = {k * l}", end = " ")
