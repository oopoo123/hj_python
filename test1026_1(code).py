str = "Korea"

str_e = str.encode("utf-8") # 통신을 위한 바이트 문자열로 변환(유니코드 문자열 -> 바이트 문자열)
print(str_e)
print(type(str_e))

str_d = str_e.decode("utf-8")
print(str_d)
print(type(str_d))

str2 = "대한민국"

str_e2 = str2.encode("utf-8")
print(str_e2)
str_e3 = str2.encode("euc-kr")
print(str_e3)
str_d2 = str_e2.decode("utf-8")
print(str_d2)