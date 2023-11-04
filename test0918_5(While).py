# '열 번 찍어 안 넘어가는 나무 없다' 속담 구현

treeHit = 0 # 나무를 찍은 횟수

while treeHit < 10: # 나무를 찍은 횟수가 10보다 작은 동안만 반복
    treeHit = treeHit + 1 # 반복 될때마다 treeHit값이 1씩 증가
    print(f"나무를 {treeHit}번 찍었습니다") # f 스트링 활용

if treeHit == 10:
    print("나무가 넘어갑니다!!!")
else:
    print("나무가 넘어가지 않습니다!!!")


while treeHit < 20:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다")
    if treeHit == 10: # 10일때 찍힘
        print("나무가 넘어갑니다!!!")
        break #while 문을 탈출하는  문
              # 강제로 while 문을 빠져나감 (while문 멈춤)


while True:
    print("break전!!!")
    break
    print("break후!!!")