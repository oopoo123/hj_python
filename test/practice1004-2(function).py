# 2. 아래 리스트를 입력받아 짝수만 포함하는 리스트를 반환하는 함수를 작성하시오
# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# 함수 이름은 evenlist()
#
# 예) list2 = evenlist(list1)
# 출력 >
# [2, 4, 6, 8]

list1 = [1, 2, 3, 4, 5, 6, 7, 8]

def evenlist(sample_list):
    mylist = []
    for i in sample_list:
        if i % 2 == 0:
            mylist.append(i)

    return mylist

list2 = evenlist(list1)

print(list2)