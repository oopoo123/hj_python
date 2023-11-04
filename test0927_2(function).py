
def add_many(*score): # *은 score를 튜플 형태로 바꿔줌
    for i in score: # (10, 20, 30, 40, 50)->튜플이 자동으로 생성됨
        print(i)

    return i

def add_many2(a, b, c, d, e):
    score = [a, b, c, d, e]
    for i in score:
        print(i)
    return i

add_many(10, 20, 30)

val1 = add_many(10, 20, 30)

val2 = add_many2(10, 20, 30, 40, 50)

print(val1)