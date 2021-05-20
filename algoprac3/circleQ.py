# import sys
# from collections import deque

# input =sys.stdin.readline


# n,m = map(int, input().split())

# nums = list(map(int, input().split()))

# que = deque([i for i in range(1,n+1)]) # 1 ~ 10


# cnt = 0

# while True:
#     for q in que:
#         for num in nums:
#             if q != num: # 다르다면
#                 que.rotate(-1)
#                 cnt += 1
#             elif num > len(q)//2:
#                 que.r()
            
#             else:         # 같다면
#                 que.popleft()
#                 que.rotate(-1)
#     if cnt == len(nums):
#         break 
        
# print(que)



# for i in q:
#     cnt = 1
#     for num in nums:
#         if i != nums:
#             q.popleft()
#             cnt += 1
#         else:
#             cnt = 0


# print(cnt)



# import sys
# from collections import deque
# n, _ = map(int, sys.stdin.readline().split())
# numbers = list(map(int, sys.stdin.readline().split()))
# queue = deque(range(1, n+1))

# total_compute = 0

# for idx in range(len(numbers)): # 123 = 3
#     if numbers[idx] == queue[0]: #numbers[0]  == queue[0] 1 / 같죠? 
#         queue.popleft() #같으니까 팝레프트
#         continue # 계속
#     queue_idx = queue.index(numbers[idx]) # 

#     # 뒤 -> 앞으로 옮기는 게 이득인 경우
#     if queue_idx > len(queue) // 2:
#         queue.rotate(len(queue) - queue_idx)
#         total_compute += (len(queue) - queue_idx)
        
#     # 앞 -> 뒤로 옮기는 게 이득인 경우
#     elif queue_idx <= len(queue) // 2:
#         queue.rotate(-queue_idx)
#         total_compute += queue_idx
#     queue.popleft()
    
# print(total_compute)


import sys
from collections import deque
n, _ = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split())) # 2,9,5
queue = deque(range(1, n+1)) # 1 ~ 10

total_compute = 0

for idx in range(len(numbers)): # 123 = 3
    if numbers[idx] == queue[0]: #numbers[0]  != queue[0] 2/1 /다르다 
        queue.popleft() #같으니까 팝레프트
        continue # 계속

    queue_idx = queue.index(numbers[idx]) # 

    # 뒤 -> 앞으로 옮기는 게 이득인 경우
    if queue_idx > len(queue) // 2: 
        queue.rotate(len(queue) - queue_idx)
        total_compute += (len(queue) - queue_idx)
        
    # 앞 -> 뒤로 옮기는 게 이득인 경우
    elif queue_idx <= len(queue) // 2:# 2의 인덱스 값은 2 < 5
        queue.rotate(-queue_idx)
        total_compute += queue_idx
    queue.popleft()
    
print(total_compute)

