N = int(input())
 
# def factorial(N):
#     if N == 0:
#         return 1
#     elif N == 1:
#         return 1
#     return N * factorial(N-1)
 
# print(factorial(N))
v = 1

for i in range(1,N+1):
    if N == 0:
        v = 1
    elif N == 1:
        v = 1
    elif N > 1:
        
        v = v*i

print(v)
   