T = int(input())

nums = [] 

for _ in range(T):  
    C = int(input()) 
    nums.append(C) 
    
for i in sorted(nums): 
    print(i)