from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

stk = deque([]) 

for i in range(T):
    c = input().split()

    if c[0] == 'push':
        stk.append(c[1])
    elif c[0] == 'pop':
        if len(stk) > 0:
            print(stk.popleft())
        else:
            print(-1)
    elif c[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == 'front':
        if len(stk) > 0:
            print(stk[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if len(stk) > 0:
            print(stk[-1])
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(stk))    
    
        
        

