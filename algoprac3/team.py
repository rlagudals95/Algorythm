num = list(map(int, input().split()))

sum = 0
num_list = []
for i in num:
    if len(num) == 5:
        sum+=i**2
        num_list.append(sum)    

print(num_list[-1]%10)