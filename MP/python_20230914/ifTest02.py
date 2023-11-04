a = [1,2,3,4,5,6]

if 3 in a:
    print("성공!")
else:
    print("실패!")
    
str = "korea"

if 'k' in str:
    print("성공!")
else:
    print("실패!")

b = ('a', 'b', 'c')

if 'd' not in b:
    print("성공!")
else:
    print("실패!")


# 수우미양가 출력 프로그램

score = 75

if score >= 90:
    print("수")
else:
    if score >= 80:
        print("우")
    else:
        if score >= 70:
            print("미")
        else:
            if score >= 60:
                print("양")
            else:
                print("가")

score = 10

if score >= 90:
    print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else:
    print("가")

ki = 1000

if ki >= 1000:
    data = 500
else:
    data = 600

print(data)