# import sys

# input = sys.stdin.readline

# N = int(input())


# YS = list(map(int, input().split()))


# for i in range(N):
#     if N % YS[i] == 0:
#         print(2*max(YS))

n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)


    