import sys

input = sys.stdin.readline

T = int(input())

stk = []

for i in range(T):
    c = input().split()

    if c[0] == 'push': # input().split() 값도 정렬 순서로 선택가능
        stk.append(c[1])
    elif c[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif c[0] == 'size':
        print(len(stk))
    elif c[0] == 'empty':
        if len(stk)> 0:
            print(0)
        else:
            print(1)
    elif c[0] == 'top':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])