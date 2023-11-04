a = [1, 2, 3, 4, 5, 6]

if 3 in a:
    print("성공!")
else:
    print("실패!")

str = "korea"

if "k" in str:         # str안에 k가 잇으면 참
    print("성공!")
else:
    print("실패!")


b = ("a", "b", "c")

if "d" not in b:      # str안에 d가 없어서 참 만약 b라면 안에 b가 있으므로 거짓
    print("성공!")
else:
    print("실패!")


# 수우미양가 출력 프로그램

score = 45

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



score = 95

if score >= 90:
    print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else:              # else 아닌애들은 다 "가" 조건 아닌 나머지 몽땅 다
    print("가")


ki = 100

if ki >= 1000:
    data = 500
else:
    data = 600

print(data)

# for문 첫번째 장벽
