a = 100
money = 1000

if money >= 2000:
    print("성공!!!!")
    print("축하합니다!!!!")
#        print("한칸더!") 에러!
else:
    print("실패!!!!")
    print("위로합니다!!!!")


x = 10
y = 20

if x != y: #!= 같지 않다
    print("x와 y는 같다!")
else:
    print("x와 y는 같지 않다!")

x = 10
y = 20

if x >= 10 or y >= 50: #or -> 두 조건 중 한개만 참이면 참 출력
    print("성공!")
else:
    print("실패!")

if x >= 10 and y >= 50: #and -> 두 조건이 모두 참이어야만 참 출력
    print("성공!")
else:
    print("실패!")

if not x >= 1 and y >= 1:
    print("성공!")
else:
    print("실패!")