import re
import requests ## requests 다운
from bs4 import BeautifulSoup ## beautifulsoup4를 다운


test_html = requests.get("https://m.yes24.com/Event/EventWinnerDetail?iContentNo=59080&NoticeYn=Y")
soup = str(BeautifulSoup(test_html.text, "html.parser"))
#파싱하기 = 분리하기
pattern = re.findall(r"[a-z0-9]+\*{3}", soup)
#r -> raw string 순수한 문자

for i in pattern:
    print(i)

# print(test_html) # 응답 확인 <Response [200]> 잘받았다 200은 바뀔수 있음
#
# print(test_html.text)
#
# print(soup)
