# n, m = map(int, input().split())
# tree = list(map(int, input().split()))

# start, end = 1, max(tree)

# while start <= end: #스타트가 엔드랑 같다는 것은 미드부분이 정해졌단것
#     mid = (start+end)//2 # 여기선 10.5 정도로 계산됨
#     log = 0
#     for i in tree:
#         if i >= mid:
#             log += i - mid # 나무들 크기가 미드보다 크면 미드 만큼자른 나무를 로그에 넣어줘!
    
#     if log >= m:
#         start = mid + 1 #나무가 많거나 같다 오른쪽으로 좁혀! - 스타트는 오른쪽으로
#     else:
#         end = mid - 1 #나무가 적다 왼쪽으로 좁혀 - 엔드는 중간에서 왼쪽으로

n, m = map(int, input().split())

tree = list(map(int,input().split()))

start, end = 1, max(tree)

while start <= end :
    mid = (start + end)//2
    log = 0

    for i in tree:
        if i > mid:
            log += i - mid
    
    if log >= m:
       start = mid + 1
    else:
        end = mid - 1 
        