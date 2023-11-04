import traceback

def a():
    return 10/0 # 0나누기 에러

def b():
    a()

def main():
    try:
        b()
    except:
        print("오류가 발생했습니다!!!")
        print(traceback.format_exc()) # 에러의 위치를 찾아줌

main()
