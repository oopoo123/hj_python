f = open("새파일2.txt", 'r')

for i in range(1, 11):
    a = f.readline()
    print(a)

f.close()

