class Shape:
    def __init__(self, width, height, colar):
        self.width = width
        self.height = height
        self.colar = colar

    def area(self):
        area = self.width * self.height
        return area

    def colar(self):
        print(f"도형의 색은 {self.colar()}색 입니다!!!")

#s1 = Shape(100, 200, "빨강")


class Circle(Shape):
    def area(self): # 메소드 오버라이딩
        area = self.width * self.width * 3.14
        return area

c1 = Circle(100, 200, "파랑")

print(c1.area())

