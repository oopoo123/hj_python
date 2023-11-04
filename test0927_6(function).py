
a = 1 # 전역변수 a

def vartest(a):
    a = a + 1 # 지역변수 a

vartest(a)

print(a)
