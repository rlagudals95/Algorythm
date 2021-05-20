input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for num in array:  # num을 반복문으로 계속 뽑아내
        if num > max_num:  # 넘이 맥스넘보다 쿨때 까지 계속 뽑아
            max_num = num

    return max_num


result = find_max_num(input)
print(result)

for num in num_list:
    if num > max_number:
        max_number = num

