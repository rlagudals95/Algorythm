cards = int(input())
nums = map(int, input().split())

cards2 = int(input())
nums2 = map(int, input().split())

one = []
two = []

for i in nums:
    one.append(i)
    for j in nums2:
        two.append(j)


v = set(one) & set(two)

for x in two:
    for vv in v:
        if x == vv:
            x == 1
        else:
            x == 0
            print(two)
       


       

            
            

            

        



# one = []
# two = []

# for i in nums:
#     one.append(i)

# for j in nums2:
#     two.append(j)
        
# if 

# print(one)
# print(two)

