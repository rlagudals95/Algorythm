# from collections import deque

# import sys

# input = sys.stdin.readline

# T = int(input())

# stk = deque([])

# for i in range(T):
#     c = input()

# while len(stk):

#     if c[0] == c[-1]:
#             stk.popleft()
#             stk.pop()
#     else:
#         stk.append(1)

#     if len(stk) == 0 :
#          print('YES')
#     else: 
#         print('NO')
    

a = int(input()) # 테스트 케이스
for i in range(a):

    b = input() # 
    s = list(b) #괄호 입력값
    
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
