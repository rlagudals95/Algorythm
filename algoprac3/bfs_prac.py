from collections import deque

def bfs(graph, start, visited):
    # 큐(Qeueu) 구현을 위해 deque 라이브러리 사용
    qeueu = deque([start])
    # 현재 노드를 방문처리
    visited[start] = True
    # 큐가 비어있을때 까지 반복
    while qeueu: # False # [2,3,8] for문을 한번 다돌면 while로 복귀
        #큐에서 하나의 원소를 뽑아 출력하기
        v = qeueu.popleft()
        print(v, end=' ')
        #아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                qeueu.append(i)
                visited[i] = True  

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7],
]

visited = [False]*9 # [False] 9개

bfs(graph,1,visited)
