# # 피보나치 함수

# def fib_naive(n):
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         fib = fib_naive(n-1) + fib_naive(n-2)
#         return fib


# # 다이나믹 프로그래밍

# n = int(input())

# fib_arry = [0,1] # 

# def fib_recur_dp(n):
#     if n < len(fib_arry): # n 이 fib_arry 안에 있으면?
#         return fib_arry[n]
#     else:
#         fib = fib_recur_dp(n-1) + fib_recur_dp(n-2) # n이 없으면 피보나치 계산을해서
#         fib_arry.append(fib) # 피보 어레이 안에 넣어준다
#         return fib

# print(fib_recur_dp(n))


# def fib(n, lookup):
#     if n <= 1:
#         return n

#     targetValue = lookup[n] # lookup[60]
#     print("targetValue:", targetValue)

#     return fib(n-2, lookup) + fib(n-1, lookup)

# lookup = [None]* (2 + 1) 
# print(lookup)
# print(fib(2 ,lookup))



# MAX = 21

# dp = [[[0]*MAX for _ in range(MAX)] for __ in range(MAX)]

# for __ in range(MAX):
#     for _ in range(MAX):
#         dp.append([0]*MAX)



# new_words = []

# for word_list in words:
#     for word in word_list:
#         if len(word) > 4:
#             new_words.append(word)
 



# new_words = [ word for word_list in words for word in word_list if len(word) > 4]




#문제에서 봤던 공식을 적용
#


MAX = 21    # 0 ~ 20 이 범위이기 때문에 21로 범위를 잡아준다.

# 입력값이 abc 세개 이기 때문에 범위를 3차 배열로 형성
dp = [[[0] * MAX for _ in range(MAX)] for __ in range(MAX)] 
# dp테이블에는 각 계산값이 담기는 형태로 들어간다.

def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 값이 이미 존재한다면 그 값을 바로 리턴한다.
    if dp[a][b][c]:
        print(f'dp[{a}][{b}][{c}] = {dp[a][b][c]}')
        return dp[a][b][c]

    if a < b < c:
        print(f'a<b<c 의 경우이다. dp[{a}][{b}][{c}]')
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    print(f'그밖의 경우 의 경우이다. dp[{a}][{b}][{c}]')
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
        w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


while True:
    a, b, c = map(int, input().split())

    # 재귀함수를 멈추는 조건
    if (a, b, c) == (-1, -1, -1):
        break

    # 출력방식은 변경 가능하다.
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))