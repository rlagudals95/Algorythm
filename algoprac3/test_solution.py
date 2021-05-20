# 이분 탐색을 이용해야 하는 문제!
# 이분탐색을 위해서 집합 N을 먼저 만들어준다!
# 시작하는 지점과 끝 지점의 인덱스 값을 지정
# 중간 값과 요소를 비교
# 값이 같다면 찾았다!
# 값이 중간 값보다 크면 => 중간보다 윗부분을 탐색 [ mid =>>]
# 값이 중간 값보다 작다면 => 중간보다 앞쪽 부분 탐색 [ <<= mid ]
# 예외로 전체 리스트에서 찾을 수 없다면 없다는 것으로 판별

import sys

input = sys.stdin.readline

n = input()
N = sorted(map(int, input().split()))
m = input()
M = map(int, input().split())

def binary(i, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2 # 중간값 설정
    if i == N[m]:
        return 1
    elif i < N[m]:
        return binary(i, N, start, m-1) # 왼쪽으로 탐색
    else: 
        return binary(i, N, m+1, end) # 오른쪽으로 탐색


for i in M:
    start = 0
    end = len(N)-1
    print(binary(i, N, start, end))