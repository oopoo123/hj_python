a = 100
b = 200

if a > 10 or b > 1000: # or은 두 조건중 하나만 참이여도 참
    print("성공!!!")
else:
    print("실패!!!")

if a > 10 and b > 1000: # and는 두 조건이 모두 참일때만 참
    print("성공!!!")
else:
    print("실패!!!")

if not a > 100:         # not는 부정하는 것이 맞다면 참
    print("성공!!!")
else:
    print("실패!!!")



