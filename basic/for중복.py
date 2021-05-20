# # 주사위 2개를 동시에 던졌을 때 나올 수 있는 경우의 수를 모두 구하시오
# # 실제로 던질때 경우의 수는 1 1, 1 2, 1 3, 1 4, 1 5, 1 6 ~~ 6 6까지 출력된다

# # 주사위1 은i // 주사기2 는 j

# count = 0

# for i in range(1,7):
#     for j in range(1,7):
#         count += 1
#         print(i,j) #경우의 수
#         print(count) # 경우의 갯수


# # 주사위 2개를 던지면? 단 주사위 면의 수가 6개가 아니다..

# n, m = map(int, input().split())

# for i in range(1,n+1):
#     for j in range(1,m+1):
#         print(i,j)

# 물감만들기 세가지 물감을 섞었을 때 나올 수 있는 경우의 수
# 물감의 갯수에 따라 출력 값이 달라진다
r,g,b = map(int, input().split()) 

count = 0

for rr in range(r): # 0~r-1
    for gg in range(g): # 0~g-1
        for bb in range(b): # 0~b-1
            count += 1
            print(rr,gg,bb)

print(count)