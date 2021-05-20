N, M = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 1, max(tree) # 이분탐색 검색 범위 설정 // 스타트는 = 1, 끝은 트리리스트중 가장큰 것 

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end)//2 # 1 + 제일큰 나무 길이 더한것 나누기 2
    log = 0 #벌목된 나무들의 총합
    for i in tree:
        if i >= mid:
            log += i - mid # 나무길이들 중에 미드 값보다 크거나 같으면 로그에 i에 미드길이 뺀걸 더해주라
    #벌목 높이를 이분탐색
    if log >= M: # 나무 길이 총합이 요구하는 나무 길이랑 같거나 크다면
        start = mid + 1 # 오른쪽에서 찾아 범위가 1이 아니라 중간에서 +1
    else:
        end = mid - 1 #아니면 왼쪽에서 찾아 1개씩 좁혀가면서

print(end)
