
age = input("나이를 입력하세요:") #주의 input문은 입력된 값을 문자열로 반환

try:
    age2 = int(age) + 10
except:
    print("나이는 숫자만 입력 됩니다")
else: # 오류가 발생하지 않았을 경우에만 실행!
    print(f"당신은 10년후에 {age2}살이 됩니다.")


