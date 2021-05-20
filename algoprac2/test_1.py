import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list2 = sorted(n_list) # [1,2,3,4,5]

m = int(input())
m_list = list(map(int, input().split())) # [1,3,7,9,5]

new = []

for i in range(len(n_list2)):
        if n_list2[i] == m_list[i]:
            new.append(1)
        elif n_list2[i+1] == m_list[i]:
            new.append(1)  
        else:
            new.append(0)

print(new)