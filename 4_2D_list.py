# 생성
arr = [[0] * m for _ in range(n)]
# arr = [[0] * m] * n => 모든 행이 같은 객체

# 방향 이동 (BFS, DFS)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < m: # 범위 체크

# max / min
max_val = max(map(max, arr))
min_val = min(map(min, arr))

# 행/열 합
row_sum = [sum(row) for row in arr]
col_sum = [sum(col) for col in zip(*arr)]

# flatten: 2차원 → 1차원
flat = [x for row in arr for x in row]

# 전치 (transpose)
transposed = list(zip(*arr))