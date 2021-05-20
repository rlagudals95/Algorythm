n = int(input())

p = list(map(int, input().split()))

arr = sorted(p) # 1,2,3,3,4

num = 0
for i in range(n):
    for j in range(i+1):
        num +=arr[j]
    
print(num)




