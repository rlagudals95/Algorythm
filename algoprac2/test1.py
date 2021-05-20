N = int(input())
cards = list(map(int, input().split()))

M = int(input())
nums = list(map(int, input().split()))

cards.sort()

for i in range(M):
    low,high = 0,N-1
    while low < high:
        mid = (low+high)//2
        if cards[mid] == nums[i]:
            print(1, end='\n')
        elif cards[mid] < nums[i]:
            low = mid + 1
        else:
            high = mid +1

        if low > high:
            print(0, end="")
            break



