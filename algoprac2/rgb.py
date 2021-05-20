# 이 문제의 포인트는 i번째가 빨강 색일 때 i-1번째의 파랑과 초록의 값 중에 작은 값을 고르는 문제


import sys

input = sys.stdin.readline

n = int(input())

RGB = [] #RGB 정렬엔 입력한 3개 요소가 포함된 정렬이 들어간다

for i in range(n):
    RGB.append(list(map(int, input().strip().split())))

for i in range(1, n):
    #빨간집
    RGB[i][0] = min(RGB[i - 1][1], RGB[i - 1][2]) + RGB[i][0]
    #ex) 26 40 83 / 49는 = 
    # 1번째 정렬의 0번 값은
    # 제일작은값 (0번째 정렬의 두번째 요소 , 0번째 정렬의 세번째 요소) + 1번째 정렬에 0번째요소

    #초록집
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    #파란집
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]

print(RGB)
print(min(RGB[n-1]))

# min = 정렬줄에 가장 작은값
# strip([chars]) : 인자로 전달된 문자를 String의 왼쪽과 오른쪽에서 제거합니다.
# 양쪽 공백도 지워짐
# > text = ' Water boils at 100 degrees '
# print(text.strip(' degrees '))
# Water boils at 100

# 원동균 / 27조 / 1149
# RGB의 최단경로를 찾아봅시다.
# 어렵게 생각하지 말고, RGB의 최단경로를 한꺼번에 구해서 min()함수를 사용해 최소값을 구해봅시다.
# 집이 1채만 있다면, R, G, B 중에 최소값을 반환하면 됩니다.
# 만약 2채 이상있다면, 다음 집을 기준으로 그 집의 전집의 각각의 R, G, B 값을 더해서 메모이제이션에 넣습니다. (물론 인접한 집은 색깔이 겹치면 안됩니다.)
# 메모이제이션에  넣으면, 앞으로 연산할때 추가 연산 필요없이 해당 배열 위치의 값만 가지고 오면 뚝딱 만들 수 있습니다.

# import sys

# n = int(sys.stdin.readline().split()[0])
# memo = [[0 for _ in range(3)] for _ in range(n)]

# def alg(num, r, g, b) :
    
#     if num == 1 :
#         return min(memo[num - 1][0], memo[num - 1][1], memo[num - 1][2])
#     for i in range(1, num) :
#         memo[i][0] = min(memo[i - 1][1], memo[i - 1][2]) + memo[i][0]
#         memo[i][1] = min(memo[i - 1][0], memo[i - 1][2]) + memo[i][1]
#         memo[i][2] = min(memo[i - 1][0], memo[i - 1][1]) + memo[i][2]
        
#         if i == num - 1 :
#             return min(memo[i][0], memo[i][1], memo[i][2])

# arr = []

# for i in range(n) :
#     red, green, blue = map(int, (sys.stdin.readline().split()))
#     memo[i][0] = red
#     memo[i][1] = green
#     memo[i][2] = blue

# print(alg(n, red, green, blue))