# *****

for i in range(5): # 0~4 5번 회전
    print("*", end="") # end 줄바꿈 \n 삭제

print("-------------------------------")

# *
# *
# *
# *
# *

for i in range(5):
    print("*")


print("-------------------------------")


# *****
# *****
# *****
# *****
# *****

for i in  range(5): # 별의 줄을 결정(행)
    for j in range(5): # 별의 개수(열)
        print("*", end="")
    print("")


print("-------------------------------")


# *
# **
# ***
# ****
# *****

for i in range(5): # 0 1 2 3 4
    for j in range(i + 1):
        print("*", end="")
    print("") #한줄씩 줄 바꿈


print("-------------------------------")


# *****
# ****
# ***
# **
# *

for i in range(5): # 돌아가는 행 개수
    for j in range(5 - i):
        print("*", end="")
    print("")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")


print("-------------------------------")

# ******
#   ****
#    ***
#     **
#      *

for i in range(5):
    for j in range(i): # *앞의 공백
        print(" ", end="")
    for j in range(5 - i):
        print("*", end="")
    print("")

            