
strs = ["10.3", "5.7", 3.14, 8.1, "10.9"]
#
# for i in strs:
#     print(int(i))

# 위의 프로그램에서 문자열 원소가 정수로 변환될때 에러가 발생됩니다
# 예외처리를 통해 에러가 발생하는 경우
# "문자열은 정수로 변환할 수 없습니다"로 출력하세요

for i in strs:
    try:
        print(int(i))
    except:
        print("문자열은 정수로 변환할 수 없습니다")

print("-----------------------------")

data = [1, 2, 3]

# for i in range(1, 5):
#     print(data[i])

# 위의 프로그램에서 인덱스 에러가 발생됩니다.
# 예외처리를 통해 에러가 발생될 때 에러의 종류(에러 이름)을
# 출력하도록 작성하세요

for i in range(1, 5):
    try:
        print(data[i])
    except Exception as e:
        print(e)




