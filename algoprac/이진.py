# 27강 이진 타색 기초문제풀이
#중간점의 값을 시간이 지날수록 최적화된 값 이진탐색을 하면서 얻을 수 있는 떡의 길이 합이 
#필요한 떡의 길이보다 크거나 같을때 중간값을 기록해주면 되겠다

#떡의 개수 n 과 요청한 떡의 길이 m을 입력
n, m = list(map(int, input().split()))
#각 떡의 개별 높이 정보들 입력
array = list(map(int, input().split()))

# 이진 탐색을 하기위한 시작점과 끝점
start = 0
end = max(array) #입력받은 값중 가장 긴 떡의 길이

#이진 탐색 수행
result = 0

while(start <= end):
    total = 0
    mid = start+end //2 # 현재 떡을 자르는 높이
    for x in array: # 잘랐을 때 떡의 양 계산
        if x > mid: # 떡의길이가 높이보다 클때 
            total += x - mid # 잘린부분의 떡을 total 변수에 담을 수 있도록해서 
    # 떡의 양이 부족할 때 더자르기 // 왼쪽 부분 탐색
    if total < m:
        end = mid-1
    # 떡의 양이 충분할 때 덜 자르기 // 높이값을 높여서 덜 자르게 만듬 // 오른쪽 탐색
    else:
        result = mid # 최대한 덜 잘라쓸 때가 정답이므로 result로 ㄱㄱ
        start = mid + 1 # 

print(result)