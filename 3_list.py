# 생성
arr = [1, 2, 3]
arr = []
arr = [0] * 5  # [0, 0, 0, 0, 0]

arr = list(range(5))  # [0,1,2,3,4]
arr = list(range(1, 6))  # [1,2,3,4,5]
arr = list(range(0, 10, 2))  # [0,2,4,6,8]

# 리스트 컴프리헨션
arr = [x for x in range(5)]
arr = [x for x in range(10) if x % 2 == 0]
arr = [x for x in arr if x > 0]

# 입력으로 리스트 생성
#   한 줄 입력
arr = list(map(int, input().split()))
arr = list(input())

#   여러 줄 입력
n = int(input())
arr = [int(input()) for _ in range(n)]

# 추가
arr = [1, 2]
arr.append(3)  # [1, 2, 3], O(1)
arr.insert(0, 3)  # O(n)

# 삭제
arr = [1, 2, 3]
arr.pop()  # 맨 마지막 제거, O(1)
arr.pop(0)  # 특정 위치 제거, O(n)
arr.remove(2)  # 값으로 삭제, 없으면 ValueError 발생

# 정렬
#   원본 수정
arr = [3, 1, 2]
arr.sort()  # [1, 2, 3]
arr.sort(reverse=True)  # [3, 1, 2]

str_list = ["one", "two", "three", "four"]
str_list.sort(key=len)  # 문자열 길이가 긴게 맨 뒤로 감 ['one', 'two', 'four', 'three']
print(str_list)

#   원본 유지
arr = [3, 1, 2]
new_arr = sorted(arr)

# 거꾸로 뒤집기
arr.reverse()   # 원본 수정, 반환값 없음 (None)
new_arr = arr[::-1]  # reverse() 보단 이걸 많이 씀

# 리스트 복사
# shallow copy (얕은 복사) => 2차원 배열에서 값 수정 시 원본, 복사본 다 바뀜
#   b = arr[:]
#   b = list(arr)

# Deep copy (깊은 복사)
import copy
b = copy.deepcopy(arr)

# 반복문
for index, value in enumerate(arr):

# 조건문
if 3 in arr:    # O(n)

# max / min / sum / 최대값
max(arr)
min(arr)
sum(arr)
max(arr, key=lambda x: x[1])

# 탐색에 .index(), .count() 쓸 수 있지만 큰 데이터에서는 느릴 수 있기 때문에 dic 사용

# 리스트 합치기
a = [1, 2]
b = [3, 4]
a.extend(b)  # [1, 2, 3, 4]
a.append(b)  # [1, 2, [3, 4]]

# flatten: 2차원 배열 -> 1차원 배열
flat = [x for row in arr for x in row]

# unpacking
a, b, c = [1, 2, 3]

# zip
a = [1, 2]
b = ["a", "b"]
list(zip(a, b))  # [(1, 'a'), (2, 'b')]
