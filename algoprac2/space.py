T = int(input())

k, end = map(int, input().split())

거리 = end - k # 3, 5 , 5

cnt = 0


while True:
    
    print(cnt)
    k += 1    
    횟수 =  1 + (k) + 1 
    cnt += 1  
    
    if 거리 - 횟수 == 0 :   
        break
     


    






# start + ( start + 1 )+ ( start + 1 )+ ( start + 1 )+ ( start + 1 )  +1