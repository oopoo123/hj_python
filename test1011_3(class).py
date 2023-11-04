
class ShapeArea:

    def triangle(self, width, height): # 삼각형의 넓이를 반환하는 메서드
        area = width * height * 0.5
        return  area

    def square(self, width, height): # 사각형의 넓이를 반환하는 메서드
        area = width * height
        return area

    def circle(self, radius): # 원의 넓이를 반환하는 메서드
        area = radius * radius * 3.14
        return area

s1 = ShapeArea() # 객체를 선언
area = s1.circle(10) # s1 객체를 만들어준 ShapeArea클래스내에 설계된 메서드를 호출

print(area)
