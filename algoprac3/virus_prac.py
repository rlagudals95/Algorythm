# from collections import deque
# #컴퓨터 수 입력받기
# n=int(input())

# #연결된 쌍수 입력받기
# pair=int(input())

# computer=[]
# for i in range(n+1):
#   computer.append([])


# for i in range(pair):
#   a,b=map(int,input().split())
#   computer[a].append(b)

# #바이러스 감염여부 확인할 리스트 만들기
# virus=[0]*(n+1)
# virus[1]=1

# #bfs 함수 만들기
# def bfs(computer):
#   queue=deque()
#   queue.append(1)
#   count=0
#   #큐가 진행되는 동안
#   while queue:
#     v=queue.popleft()
#     #현재 주어진 컴퓨터에 연결된 컴퓨터 찾기
#     for com in computer[v]:
#       if virus[com]==0:
#         virus[com]=1
#         queue.append(com)
#         count+=1
#   return count

N = int(input()) # 버텍스
P = int(input()) # 라인
# 인덱스 번호 맞추기 위해 한 줄 추가
graph = [[0]*(N+1)for _ in range(N+1)] # [0,0,0,0,0,0,0] 7개
visited = []

for _ in range(P):
    x,y =map(int, input().split())
    graph[x][y],graph[y][x] = 1,1 # 

def dfs(v):
    visited.append(v)
    for i in range(1,N + 1): # 1 ~ n 번까지
        if (i not in visited) and (graph[v][i] == 1):
            dfs(i)
    return(len(visited) - 1) # 1번을 제외한 컴퓨터 수

print(dfs(1))

    