f = open("새파일2.txt", 'r')

while True: # 무한루프
    a = f.readline()
    if not a:
        break
    print(a)

f.close()