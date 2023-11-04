
# 1. 어느 학교의 학점 기준이 아래와 같을때, 사용자로부터 score를 입력받아
# 학점을 출력하는 프로그램을 작성 하시오(if문, input문 사용)
#
#
# 점수      학점
# 81~100    A
# 61~80     B
# 41~60     C
# 21~40     D
# 0~20      E

# a = input() 변수를 또 만드는것 보다 밑에 처럼 그냥 덮어 씌어주는게 더 좋다
score = input("당신의 성적을 입력하세요:")
score = int(score)

if score > 80: # 81 <= score <= 100 파이썬에서만 사용가능
    print("A")
elif score > 60:
    print("B")
elif score > 40:
    print("C")
elif score > 20:
    print("D")
else:
    print("E")



