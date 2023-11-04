# 문자열 함수 알아보기 (2023년 9월 7일)
a = "안녕하세요!!"

# print(a[3])

print(a.count("세")) # a 문장안에 세가 하나라서 1개가 뜬다
print(a.count("!")) # a 문장안에 !가 두개라서 2가 뜬다
# 글자를 찾을수 있다 안녕이라고 하면 1개가 뜬다
# 해당 문자열 안에 있는 특정 문자의 개수 반환

print(",".join("ABCD")) # join , 객체 글 하나하나에 ,를 넣어준다

print(a.find("세")) # 찾는 문자의 위치 반환
print(a.find("감")) # 찾는 문자가 없으면 -1 반환
print(a.find("!"))  # 첫번째 찾는 문자의 위치 반환

print(a.index("세")) # 찾는 문자의 인덱스를 반환
# print(a.index("감")) # 찾는 문자가 없으면 에러!

str1 = "Korea"
str2 = "KOREA"

print(str1.upper()) # 소문자를 대문자로 변환
print(str2.lower()) # 대문자를 소문자로 변환

str3 = " hello   " # 좌 1 공백 우 3 공백 문자열

print(str3)
print(str3.strip()) # 문자열의 양쪽 공백 제거(왼쪽만 제거:lstrip, 오른쪽 제거:rstrip)

str4 = "life is too short"
print(str4.replace("life", "love")) #특정 문자열의 찾아서 새로운 문자열로 바꾸기

str5 = "affa:fadsf:ttt:rrr"

print(str5.split(":"))

