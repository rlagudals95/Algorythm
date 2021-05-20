# N = int(input())

# s= list(map(int, input().split()))

# s.sort()

# num = 0
 
# for i in range(N): # i를 5범위로 돌려준다 1,2,3,4
#     for j in range(i+1): # j를 1+1 로 돌려준다 2,3,4,5
#         num += s[j]

# print(num)

#####################

N = int(input())
nums = list(map(int, input().split()))

if N == 1 : #1
    print(nums[0])
else : 
    nums.sort() #2

    i_sum = 0 
    min_sum = 0

    for i in range(N): 
        min_sum += (i_sum + nums[i]) #3
        i_sum += nums[i] #4
        
    print(min_sum)
 
#######################

num_ppl = int(input())
waiting_time = list(map(int, input().split()))
answer = 0
waiting_time.sort()

for i in range(num_ppl):
    answer += waiting_time[i] * (num_ppl-i)

print(answer)

#####################

N = int(input())
li = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    ans += sum(li[:i+1])
print(ans)
