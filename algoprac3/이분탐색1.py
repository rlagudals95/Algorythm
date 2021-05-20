# n = int(input())

# n_list = list(map(int, input().split()))

# arr_n = sorted(n_list)

# m = int(input())

# m_list = list(map(int, input().split()))
# m_list[1] == 2

# print(n_list)
# print(m_list)


# for i in range(n):
        
#         if arr_n[i] == m_list[i]:
#             print(1)

#         else:
#             print(0)


# def BinarySearch(arr, val, low, high):
#     if low > high:
#         return False
    
#     mid = (low + high) // 2
#     if arr[mid] > val:
#         return BinarySearch(arr, val, low, mid - 1)
#     elif arr[mid] < val:
#         return BinarySearch(arr, val, mid + 1, high)
#     else:
#         return True

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# M_list = list(map(int, input().split()))
# A = sorted(A)     

# for m in M_list:
#     if BinarySearch(A, m, 0, N-1):
#         print(1)
#     else:
#         print(0)






def binary_search(a, x, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2
    if a[mid] == x:
        return True
    elif a[mid] > x:
        return binary_search(a, x, start, mid-1)
    else:
        return binary_search(a, x, mid+1, end) # [1,2,3,4,5], 5, 3+1 , 4
    

n = int(input())
a = list(map(int, input().split()))
m = int(input())
m_l = list(map(int, input().split())) #1 3 7 9 8

a = sorted(a)     # 1,2,3,4,5

for m in m_l:
    if binary_search(a, m, 0, n-1):
        print(1)
    else:
        print(0)
