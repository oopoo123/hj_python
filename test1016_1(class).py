class Score:
    def __init__(self, kor, eng, math, sci): # 생성자(초기화자)-객체가 생성될때 자동으로 호출되는 메서드
        print("안녕하세요 저는 생성자 입니다!!!")
        print("변수 초기화를 시작합니다!!")
        self.kor = kor
        self.eng = eng
        self.math = math
        self.sci = sci

    def aver(self):
        ave = (self.kor + self.eng + self.math + self.sci) / 4
        return ave

    def sum(self):
        sum = self.kor + self.eng + self.math + self.sci
        return sum

sc1 = Score(60, 100, 70, 20)

averScore = sc1.aver()
sumScore = sc1.sum()

print(averScore)
print(sumScore)

#밑에는 자식 클래스
class ScorePlus(Score):

    def maxScore(self):
        maxScore = max(self.kor, self.eng, self.math, self.sci)
        return maxScore

sp1 = ScorePlus(20, 30 ,50, 40)
print(sp1.aver())
print(sp1.maxScore()) # maxScore 메서드가 추가됨 확장의 개념

