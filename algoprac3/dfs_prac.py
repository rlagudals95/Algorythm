def dfs(graph,v,visited):
    #현재 노드를 방문 처리
    visited[v] = True # 정렬안에 값이 있다
    print(v, end=' ') # 해당 노드의 번호를 출력 (방문했다는 의미)
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: #그래프 안의 첫번째는 [2,3,8]
        if not visited[i]: # 방문되지 않은 상태라면 재귀 함수를 이용해 방문을 진행 #True 인지 False 인지 확인 False면 통과!
            dfs(graph, i ,visited) # 방문한 적이 없으면 True 로 체크하고 통과


# 각 노드가 연결된 정보를 표현(2차원 리스트)
# 해당 노드에 인접한 노드가 무엇일까?
graph = [
    [], # 인덱스 0인 부분은 비워두는게 낫다  v가 1이니 밑에서부터 시작
    [2,3,8], # 1번 노드와 연결되있는 노드
    [1,7],  # 2번 노드와 연결되있는
    [1,4,5], # 3번 노드와 연결되있는
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False]*9 #처음엔 아직 모든 노드를 방문하지 않음 False  [][True 1?][][][][][][][][][]
# 여기선 1번 노드부터 9번 노드를 가지고 있기 때문에 인덱스 0을 사용하지 않고 8+1=9를 사용

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
