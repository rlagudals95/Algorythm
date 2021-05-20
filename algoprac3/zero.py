import sys

input = sys.stdin.readline

T = int(input())

stk = []

for i in range(T):
    c = int(input())
    if c == 0:
       stk.pop()
    else:
        stk.append(c)

    
print(sum(stk)) 

