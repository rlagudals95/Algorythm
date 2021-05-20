T = int(input())


for _ in range(T):
    H, W, N = map(int, input().split())
    
    if H % N != 0: # 층수가 손님수의 배수가 아닐때
        first = N%H
        last = N/H + 1 
        
    else:
        first = H
        last = N/H 

    print(int((first*100) + last))
