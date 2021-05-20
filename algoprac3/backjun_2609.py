# C = list(map(int, input().split()))

# a = C[0] 
# b = C[1] 

    
    

# low = 6

# high = a*b//low
# low = a*b//high

# print(low,high)

import sys 

A, B = map(int, sys.stdin.readline().split()) 
# a=24 b=18
a, b = A, B 

while b != 0: 
     a = a % b # a = 24를 18로 나눈 나머지 6 // 6이 최대공약수 
     a, b = b, a # a는 6이 되어 b가 되고 6,18 = 18,6 이제 18이 또들어가 b로 나뉘면 0

print(a) 
print(A*B//a) # 최소 공배수는 두수 곱한것 나누기 최대공약수








