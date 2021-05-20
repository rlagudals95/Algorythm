def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1): # n은 1이 아니라 4였다
        if visit[i] == 0 and s[v][i] == 1: # 조건문 충족 x // 트루 & x //3. 트루//
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v] = 0
    while(queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split()) #n=4, m=5, v=1
s = [[0] * (n + 1) for i in range(n + 1)] # [0,0,0,0,0] 정렬 5개 만듦

visit = [0 for i in range(n + 1)] # [0,1,0,0,0] 생성 1번째 true
for i in range(m): # 선의 개수만큼 반복
    x, y = map(int, input().split()) #
    s[x][y] = 1 # [0,0,0,0,0],[0,0,1,1,1,][0,1,0,0,1],[0,1,0,0,1],[0,1,1,1,0]
    s[y][x] = 1 #
    
dfs(v)
print()
bfs(v)