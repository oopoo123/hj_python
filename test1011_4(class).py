class ShapeArea:

    # 객체변수(self.변수이름)를 초기화 할떄만 선언해 줌
    def __init__(self, width, height): # 초기화자(생성자)->객체가 만들어질때(선언될때)자동으로 실행
        self.width = width
        self.height = height

    def setData(self, width, height): # 객체변수를 만들어주는 메서드
        self.width = width
        self.height = height
        # self는 모든 메서드가 만들어 질때 자동으로 들어감

    def triangle(self): # 삼각형의 넓이를 반환하는 메서드
        area = self.width * self.height * 0.5
        return  area

    def square(self): # 사각형의 넓이를 반환하는 메서드
        area = self.width * self.height
        return area

    def circle(self): # 원의 넓이를 반환하는 메서드
        area = self.radius * self.radius * 3.14
        return area

s1 = ShapeArea(10, 20) # 객체를 선언
s1.setData(50, 60)

area = s1.square() # s1 객체를 만들어준 ShapeArea클래스내에 설계된 메서드를 호출

print(area) # 200 출력

s2 = ShapeArea(100, 200) #s2 객체를 선언
area2 = s2.square()
print(area2)