import time
import threading

def long_task(): # 5초의 실행시간이 소요되는 함수
    for i in range(0, 5):
        time.sleep(1) # 1초 휴식 -> 1초에 한번씩 print문 실행
        print(f"일하는중:{i}\n")

print("시작!!!")

threads = []

for i in range(0, 5):
    t = threading.Thread(target=long_task) # 함수를 스레드로 생성
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("끝!!!")

