from collections import deque

c = int(input())

arr = deque([])

for i in range(c):
    cmd = input().split()

    if cmd[0] == 'push':
        arr.append(cmd[1])

    elif cmd[0] == 'pop':  
        if not arr:
            print(-1)
        else:
            print(arr.popleft())
    elif cmd[0] == 'size':
        print(len(arr))

    elif cmd[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])

    elif cmd[0] == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
        
                
            

