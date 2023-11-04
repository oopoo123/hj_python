# 정규표현식 예제
import re # regular expression 정규표현식 표준 라이브러리

str = "Do You Have Everything With You ??!! 안녕하세요 123"

print("-----------------------")
# 영어 소문자만 출력
pattern = re.compile("[a-z]")
print(pattern.findall(str))

print("-----------------------")

# 대문자만 출력
pattern = re.compile("[A-Z]")
print(pattern.findall(str))

print("-----------------------")

# 영어 소문자를 제외한 대문자와 숫자, 한글, 특수문자 출력
pattern = re.compile("[^a-z]")
print(pattern.findall(str))

print("-----------------------")

pattern = re.compile("[a-z]+") # + 공백 빼고 다 합침
print(pattern.findall(str))

print("-----------------------")

# 한글만 출력
pattern = re.compile("[가-힣]+")
print(pattern.findall(str))

print("-----------------------")

# 주민번호 뒷자리를 *******로 치환
str2 = "991230-1234567"
pattern = "-[0-9]{7}"
print(re.sub(pattern, "-*******", str2))


