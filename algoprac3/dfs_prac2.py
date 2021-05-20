vertexList = ['0','1','2','3','4','5','6']

edgeList = [(0,1),(0,2),(1,0),(1,3)
            , (2,0), (2,4), (2,5), (3,1)  
            , (4,2), (4,6),(5,2), (6,4)]


adjacencyList = [[]for vertex in vertexList] # 리스트 안의 수만큼 []을 만든다 넣는다

# adjacencyList = [ [],[],[],[],[],[],[] ]

for edge in edgeList: # 
    adjacencyList[edge[0]].append(edge[1]) # 0,1 // 0,2

# []

# adjacencyList:
# [
#     [1,2], # //vertex 0
#     [0,3], # //vertex 1
#     [0,4,5],# //vertwx 2
#     [1], # // vertex 3
#     [2,6], # //vertex 4
#     [2], # // vertex 5
#     [4] # //vertex 6
# ]