# T = int(input())

# for _ in range(T):
#     m, n = map(int, input().split()) # m 은 13 n은 29
#     answer = 1
#     k = n - m # k = 29 - 13// k= 13
    
#     while n > k: # 29 > 13
#         answer *= n # 1곱하기 29 //28,27,26,25,24,23,22,21,20,19,18,17,16,
#         n -= 1
#     while m > 1: # 13
#         answer = answer // m #
#         m -= 1
    
#     print(answer)

def factorial(n): #
    num = 1 # num 설정
    for i in range(1, n+1): # n1무터 만큼 반복 팩토리얼 > 1부터 자기자신을 게속곱해줌
        num *= i # 곱해줌
    return num # # 1부터 자기자신까지 곱한거 반환


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n)) # 조합 29C13 표현식
    print(bridge)