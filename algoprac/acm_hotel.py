T = int(input())

# 층수 H 호수 W 손님순서 N이라고 가정
# N%H = 층수  N/H + 1= 호수  >> (N%H)*100 N/H + 1 이 손님이 묵을 방번호가 되겠다
# 근데 맨꼭대기 층일때 즉 H와 손님순서가 같을땐 그냥 H를 출력

for _ in range(T):
    H,W,N = map(int, input().split())

    if H != N:
        print(int((N%H)*100 + (N/H + 1)))
    else:
        print(int((H*100) + (N/H + 1)))



