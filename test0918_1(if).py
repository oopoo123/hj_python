a = 100

if a > 10:    # tap 들여쓰기 shift+tap 내어쓰기
    print("성공!!")
else:
    print("실패!!") # 들여쓰기가 되어 있어야지만 if문 소속

if a < 1000: # if문은 else 없이 단독으로 사용가능
    print("a는 1000보다 작아요")
# else는 옵션이다 실패시 나오게 할때 쓴다

# if else문은 조건이 하나일때만 쓰고
# elif는 여러개의 조건일때 마지막은 else로(나머지 뜻)

score = 67

if score >= 90: # 첫 번째 조건이 만족하면 바로 스탑 밑으로 안내려감
    print("수")
    print("참 잘했어요!")
elif score >= 80:
    print("우")
    print("잘했어요!")
elif score >= 70:
    print("미")
    print("분발하세요!")
elif score >= 60:
    print("양")
    print("공부하세요!")
else:
    print("가") #나머지 조건을 제외한 값은 여기에 걸려라!!
    print("남으세요!")


