# 17. 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하세요.
#
#    이름	  희망 가격
#    메로나     1000
#   폴라포	   1200
#   빵빠레	   1800

icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}

print(icecream)

# 18. 17 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하세요.
#
#    이름	 희망 가격
#  죠스바	  1200
#  월드콘	  1500

icecream["죠스바"] = 1200
icecream["월드콘"] = 1500

print(icecream)

# 19. 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
#
#   ice = {'메로나': 1000,
#          '폴로포': 1200,
#          '빵빠레': 1800,
#          '죠스바': 1200,
#          '월드콘': 1500}

print(icecream["메로나"])

#
# 20. 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
#
#   ice = {'메로나': 1000,
#          '폴로포': 1200,
#          '빵빠레': 1800,
#          '죠스바': 1200,
#          '월드콘': 1500}
#

icecream["메로나"] = 1300

# 21. 다음 딕셔너리에서 메로나를 삭제하라.
#
#   ice = {'메로나': 1000,
#          '폴로포': 1200,
#          '빵빠레': 1800,
#          '죠스바': 1200,
#          '월드콘': 1500}

del icecream["메로나"]