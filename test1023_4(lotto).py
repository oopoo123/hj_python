import random

# 원하는 게임의 수를 사용자로부터 입력 받아서
# 에) 원하는 게임의 수를 입력하세요 : 5
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]

myLotto = []

while(len(myLotto) < 6):
    lottoNum = random.randint(1, 45) # 1~45 아이의 임의의 수를 리턴
    if lottoNum not in myLotto:
        myLotto.append(lottoNum)

print(sorted(myLotto))

print("-----------------------------")

def makeLottoNum(mLotto):
    while (len(mLotto) < 6):
        lottoNum = random.randint(1, 45)  # 1~45 아이의 임의의 수를 리턴
        if lottoNum not in mLotto:
            mLotto.append(lottoNum)

count = input("원하는 게임의 수를 입력하세요: ")

for i in range(1, int(count)+1):
    mLotto = []
    makeLottoNum(mLotto)
    print(sorted(mLotto))


