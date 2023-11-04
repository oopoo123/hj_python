
def add(a, b):
    return a + b

PI = 3.141592 # 상수 ->대문자로 변수명을 선언(안변하는 값)

class Circle:
    def circleArea(self, r):
        return r * r * PI

if __name__=="__main__":
    # 본 모듈을 호출하는 파일에서 아래 명령문들이 자동으로 실행되는 것을 막음
    print(add(10, 20))
