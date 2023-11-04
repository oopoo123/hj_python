# itertools

import itertools

list1 = ["kor", "jap", "chn", "usa", "un"]
list2 = ["한글", "일본어", "중국어"]

result = itertools.zip_longest(list1, list2, fillvalue="영어")

print(list(result))

print(list(itertools.permutations(["1", "2", "3"], 2))) # 순열
print(list(itertools.combinations(["1", "2", "3"], 2))) # 조합