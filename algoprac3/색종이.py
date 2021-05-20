# import sys

# input = sys.stdin.readline

# T = int(input())

# box = []

# for i in range(T):
#     n = input().split()
#     box.append(n)

# for line in box(T):
#     line[i]

# print(box)

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
# [[1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 
# 0, 0], [1, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 
# 1, 1, 1, 1]]
result = []

def solution(x, y, N) :
  color = paper[x][y] # 페이퍼의 0번째 정렬의 0번째 요소
  for i in range(x, x+N) : # 0부터 0 + 8
    for j in range(y, y+N) : # 0부터 0 + 8
      if color != paper[i][j] : # paper[x][y] != paper[i][]
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))