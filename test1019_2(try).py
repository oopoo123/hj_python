
#파일을 불러오는 명령문은 반드시 예외처리를 해주는 것이 좋다
#파일을 불러오는 실행문은 에러가 발생할 가능성이 높기 때문

try:
    f = open("test.txt", "r") #test.txt 불러오기
    l = f.readline()
    print(l)
except:
    pass
finally:
    if f != None:
        f.close()


#가져온 파일을 실행해서 작업을 진행함