# a_list = [1,3,2,5,1,2]

# b_list = []
# for a in a_list:
#     b_list.append(a*2)

#위의 반복문을 간결하게

a_list = [1,3,2,5,1,2]

b_list = [a*2 for a in a_list]

print(b_list)
