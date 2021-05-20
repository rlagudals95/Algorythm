input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    for num in array:  # 이중 반복문
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
