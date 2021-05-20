n = int(input())

t = []
for i in range(n):
    t.append(list(map(int, input().split()))) # 리스트를 돌려준다

k = 2

for i in range(1, n): # 1부터 테스트 케이스 N만큼 돌려준다 5/ 1,2,3,4
    for j in range(k): # K는 범위가 2부터 3/4/5/
        if j == 0: # 제일 왼쪽 값들 
            t[i][j] = t[i][j] + t[i - 1][j] # 
        elif i == j: # 제일 오른쪽 값들
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else: # 요소 2개를 받아서 더 큰 것을 선택하는 경우
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
            
    k += 1

print(max(t[n - 1]))# 가장 아래층까지의 합중에서 가장 큰 값

# i번째줄을 세로번호 j는 가로번호 

