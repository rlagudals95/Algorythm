# T = int(input())

# k, end = map(int, input().split())

# 거리 = end - k # 3, 5 , 5

# cnt = 0


# while True:
    
#     print(cnt)
#     k += 1    
#     횟수 =  1 + (k) + 1 
#     cnt += 1  
    
#     if 거리 - 횟수 == 0 :   
#         break

# t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x # 이동해야 하는거리 3 , 4 , 5
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # count 수에 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)


# t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x # 3
#     count = 0  # 이동 횟수 1 2 3
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합 1 2 3
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # count 수에 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)


for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x # 3
    count = 0  # 이동 횟수  1/2/3
    move = 1  # count가 증가 할때마다 이동한거리 
    move_plus = 0  # 이동한 거리의 합 1/2/4 
    while move_plus < distance : # 
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때, 
            move += 1  
    print(count)