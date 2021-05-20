n = int(input())

arr = []

for i in range(n):
    c = input().split()

    if c[0] == 'push':
        arr.append(c[1])
    elif c[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:               
            print(arr.pop()) 
    elif c[0] == 'top':
        print(arr[-1])
        if len(arr) == 0:
            print(-1)
    elif c[0] == 'size':
        print(len(arr))
    elif c[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
      


        
    


