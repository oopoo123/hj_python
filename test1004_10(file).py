# f = open("새파일2.txt", 'r')
# f.close()

with open("새파일2.txt", 'r') as f: # close 안써도 됨 자동으로 파일 사용 후 닫음
    a = f.readline()
    print(a)
# 보통 이 방법으로 외부파일을 불러 온다

