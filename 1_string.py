# 문자열 인덱싱
s = "abcdef"
s[0]  # 'a'
s[-1]  # 'f'

# 문자열 슬라이싱
s = "abcdef"
s[1:4]  # 'bcd'
s[:3]  # 'abc'
s[3:]  # 'def'

# 문자열 뒤집기
s = "abcdef"
s[::-1]  # 'fedcba'

# 문자열 길이
len(s)

# 문자열 탐색
s.find("e")  # 있으면 1, 없으면 -1
s.index("g")  # 있으면 1, 없으면 ValueError 발생
print("e" in s)  # 있으면 True, 없으면 False (보통 이걸 많이 씀)

# 문자 개수 세기
s = "banana"
s.count("a")  # 3
s.count("an")  # 2

# 문자열 변환
s.upper()  # 대문자
s.lower()  # 소문자

s.strip()  # 양쪽 공백 제거
s.lstrip()
s.rstrip()

s.replace("a", "b")  # s에 있는 모든 a 다 바뀜
print("abcabc".replace("a", "b"))

# 문자열 분리
s = "a b c"

s.split()  # ['a', 'b', 'c']
s.split(" ")  # 동일

s = "a,b,c"
s.split(",")  # ['a', 'b', 'c']

# 문자열 합치기
arr = ["a", "b", "c"]

"".join(arr)  # 'abc'
" ".join(arr)  # 'a b c'

# 문자열 정렬
s = "dcba"

print(sorted(s))  # ['a', 'b', 'c', 'd']

"".join(sorted(s))  # 'abcd'
"".join(sorted(s, reverse=True))  # 'dcba'

# 문자열 비교
"abc" == "abc"  # True
"abc" < "abd"  # True (사전순 비교)

# 아스키 <--> 문자 변환
ord("a")  # 97
chr(97)  # 'a'
