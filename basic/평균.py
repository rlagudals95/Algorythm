T = int(input())

for _ in range(T):
    nums = list(map(int, input().split()))
    
    avg = sum(nums[1:])/nums[0]
    cnt = 0

    for score in nums:
        if score > avg:
            cnt += 1
    rate = round(cnt/nums[0]*100, 3)
    print(rate)

