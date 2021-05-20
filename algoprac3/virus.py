# import sys

# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# for i in range(n+1):
#     s = map(int, input().split())

# def dsf(graph,v,visited):
#     visited[v] = True
#     print(v, end = ' ')
#     for i in range(n+1):
#         if not visited[i]:
#             dsf(graph,v,visited)



# visited = [0 for i in range(n+1)]

# # graph = [[0]*5 for i in range(n+1)]

# v = 1

# graph = [
#     [],
#     [1,2],
#     [2,3],
#     [1,5],
#     [5,2],
#     [5,6],
#     [4,7],
# ]

# print(visited)