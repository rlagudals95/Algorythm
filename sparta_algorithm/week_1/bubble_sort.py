# 앞과 뒤를 비교하면서 작은 순서대로 정렬하는 방식

input = [4, 6, 2, 9, 1]



def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j+1]: #앞과뒤의 값비교
                array[j], array[j+1] = array[j+1], array[j] #앞과뒤의 자리비교
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!