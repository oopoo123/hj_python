# 3. 입력된 문자열을 역순으로 출력하는 함수를 작성하시오
# 함수이름은 reversePrint
# 예) reversePrint("hello")
# 출력 >
# olleh

#1
def reversePrint(str):
    strSample = ""
    for i in str:
        strSample = i + strSample

    print(strSample)

reversePrint("hello")



#2
def reversePrint2(str):
    list1 = list(str) #문자열을 리스트로 변환
    list1.reverse()

    print(list1)

reversePrint2("hello")


#3
def reversePrint3(str):
    list2 = list(str) #문자열을 리스트로 변환
    list2.reverse()

    strSample = ""
    for i in list2:
        strSample = strSample + i

    print(strSample)

reversePrint3("hello")



#4
str1 = "hello"

print(str1[::-1]) # 인덱싱으로 문자열 역순 출력



#5
def test(str):
    for i in range(len(str)-1, -1, -1): #문자열 인덱스 역순 반복
        print(str[i], end="") # 줄바꿈 기호 삭제 출력

test("hello")
