T = int(input())

nums = []

for _ in range(T):
    c = int(input())
    nums.append(c)

for i in sorted(nums) :
    print(i)
