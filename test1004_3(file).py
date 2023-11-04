
f = open("새파일2.txt", 'w')
for i in range(1, 51):
    f.write(f"{i}번째 안녕하세요!!!\n")
f.close() # 닫아주는건 꼭 해줘야한다!!!

