# n = int(input()) #n=4, m=5, v=1
# # s = [[0] * (n + 1) for i in range(n + 1)] # [false] 4개 생성
# s = [0 for i in range(n + 1)]
# print(s)

# for i in range(1, 2):
#     i += 1
#     print(i)

n, m, v = map(int, input().split()) #n=4, m=5, v=1
s = [[0] * (n + 1) for i in range(n + 1)] # [1,2][1,3][1,4][2,4][3,4]

visit = [0 for i in range(n + 1)] # [0,0,0,0,0] 생성 1번째 true
for i in range(m): # 선의 개수만큼 반복
    x, y = map(int, input().split()) #
    s[x][y] = 1 #이게 왜 1일까?
    s[y][x] = 1

print(s)
print(visit)