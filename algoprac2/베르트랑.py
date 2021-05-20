# num = int(input())

# limit = [x for x in range(num+1, (num*2))] 

# sosu = []

# for i in limit:
#     result=True
#     if(i<2):
#      result = False
#     for j in range(2,i):
#      if(i%j==0):
#       result = False
#     if result:
#         sosu.append(i)
     
# print(len(sosu))

num = int(input())

sosu = []

def new_func(sosu, i):
    if(i<2):
      result = False
    for j in range(2,i):
     if(i%j==0):
      result = False
    if result:
        sosu.append(i)

for i in range(num+1, (num*2)+1):
    result=True
    new_func(sosu, i)
     
print(len(sosu))



# n=100000

# for i in range(n+1):
#   result=True
#   if(i<2):
#     result = False
#   for j in range(2,i):
#     if(i%j==0):
#       result = False
#   if result:
#     #   print(i, end=" ")