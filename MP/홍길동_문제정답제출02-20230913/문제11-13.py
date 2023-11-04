# 11-1. 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
# 영화 제목을 movie_rank 이름의 리스트에 저장해보세요.
# (순위 정보는 저장하지 않습니다.)
#
#    순위	영화
#    1	닥터 스트레인지
#    2	스플릿
#    3	럭키
#
# 11-2. 11-1의 movie_rank 리스트에 "배트맨"을 추가하세요.

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

print(movie_rank)

movie_rank.append("배트맨")

print(movie_rank)

# 12. movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하세요.
#
#    movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
#
# 13. movie_rank 리스트에서 '럭키'를 삭제하세요.
#
#    movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

movie_rank.insert(1, "슈퍼맨")

print(movie_rank)

del movie_rank[3]

print(movie_rank)