# import sys

# input = sys.stdin.readline

# n,m = map(int, input().split())

# for i in range(n):
#     i = i+1  
#     print(i)  

# import sys

# input = sys.stdin.readline

# n,m = map(int, input().split())

# for i in range(n):
#     i = i+1
#     for j in range(n):
#         j = j+1
#         if i != j:
#             print(i,j)  

import sys

input = sys.stdin.readline

n,m = map(int, input().split())

for i in range(n):
    i = i+1
    for j in range(n):
        j = j+1
        if i != j:
            print(i,j)  