
class Triangle:
    def triArea(self, width, height):
        area = width * height * 0.5 #클래스 안에 있는 함수는 메서드라고 한다
        return area

    def triName(self, name):
        print(f"삼각형의 이름은 {name}입니다!!")

tri1 = Triangle() # Triangle 클래스로 객체를 선언

tri2 = Triangle()

area = tri1.triArea(10, 20)

print(area)

tri1.triName("홍삼각형")