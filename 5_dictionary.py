# 생성
person = {
    "name": "Jenny",
    "job": "developer",
}

# 빈 딕셔너리
d = {}
d = dict()

# 값 조회
person["name"]  #  키 없으면 KeyError 발생
person.get("name")  # 키 없으면 None 반환
person.get("address", "없음")  # 기본값 지정 가능

person["age"] = 30  # 키가 없으면 추가, 있으면 수정
person["city"] = "Seoul"  # 추가
person.update({"age": 31, "city": "Busan"})

# 삭제 => del, pop() 둘 다 키 없으면 KeyError 발생
del person["age"]
age = person.pop("age")
person.pop("age", None)  # 기본값 지정 가능 (키 없어도 에러 발생 X)
person.clear()  # 전체 삭제

# key 개수
len(person)

# 반복문
# keys(), values(), items()는 리스트가 아님!!
# list(person.keys())로 감싸줘야 리스트임!!
for key in person:
    print(key)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)

# 조건
"name" in person  # in은 key 기준

# 빈도수 세기
nums = [1, 2, 1, 3, 2, 1]
count = {}

for n in nums:
    count[n] = count.get(n, 0) + 1

#   Counter 사용
from collections import Counter

count = Counter(nums)

# 정렬
#   key 기준
sorted(count.items())
#   value 기준
sorted(
    count.items(),
    key=lambda x: x[1],
    # reverse=True,   # 내림차순
)

# 값 기준 최대값/최소값 key
max_key = max(count, key=count.get)
min_key = min(count, key=count.get)

# 복사
person2 = person.copy()

# 중첩 딕셔너리일 경우 deep copy
import copy

person2 = copy.deepcopy(person)

# 병합 (Python 3.9+)
a = {"x": 1}
b = {"y": 2}

c = a | b  # {'x':1, 'y':2}

# key/value swap
d = {"a": 1, "b": 2}
rev = {v: k for k, v in d.items()}

# defaultdict
from collections import defaultdict

d = defaultdict(int)  # int로 설정하면 초기값 자동 0으로 설정됨
d["apple"] += 1

graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)

# setdefault()
d = {}
d.setdefault("a", 0)  # 없으면 생성
d["a"] += 1
