# f-string
name = "Tom"
age = 20
print(f"{name} is {age} years old")


# 소수점 자리수
pi = 3.141592
print(f"{pi:.2f}")  # 3.14, 정수에도 .2f 쓰면 float으로 출력됨
print(f"{pi:.4f}")  # 3.1416 (반올림)


# 자리수 맞추기 (정렬) => string도 동일함
num = 42
print(f"{num:5}")  # '   42' (오른쪽 정렬)
print(f"{num:<5}")  # '42   ' (왼쪽 정렬)
print(f"{num:^5}")  # ' 42  ' (가운데 정렬)
print(f"{num:05}")  # 빈 곳 0으로 채우기 '00042'


# 천 단위 콤마
print(f"{1_000_000:,}")  # 1,000,000


# 부호 표시
num = 10
print(f"{num:+}")  # +10
print(f"{-num:+}")  # -10
