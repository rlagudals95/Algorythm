#################
# 1을 방문했을 때 2,5,9를 스택에 넣어준다
# 맨처

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}



# 1. 루트 노드를 스택에 넣는다.
# 2. 현재 스택의 노드를 빼서 visited에 추가한다
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가한다.
# 4. 2부터 반복한다
# 5. 스택이 비면 탐색을 종료한다

def dfs_stack(adjacent_graph, start_node): #그래프, 노드
    stack = [start_node] # 1
    visited = [] # 맨처음엔 1이 들어온다

    while stack: # 스택이 비어있을때 까지
        current_node = stack.pop() # 맨 뒤에껄 팝 한걸 비지트에 계속 넣어준다
        visited.append(current_node) # visited = [1] 스택의 마지막 값을 어팬드 해준다계쏙쏙
        for adjacent_node in adjacent_graph[current_node]: # 그래프의 마지막값을 빼준게 레인지 한번 빼주고 돌리고 빼주고 돌리고
            if adjacent_node not in visited: # 비지트 않에 겹치는 요소가 없을 경우에 // 있다면 그냥 팝하겠죠?
                stack.append(adjacent_node)  # 스택에 넣어준다 요소를 그리고 위에서 팝을 해준 값을 비지트에 어펜드

    return visited

print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
