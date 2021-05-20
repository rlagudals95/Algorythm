finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 최솟값 1 최댓값은 16 //  시돗값
# 최솟값이 9로 변경된다 최댓값은 16
# 최솟갚 9 더하기 최댓값16 = 24//2 >> 12
# 최솟값은 12 최댓값 16 >>28 // 2 >> 14

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array)-1
    current_guess = current_min+current_max//2 # 중간값
    find_count = 0

    while current_min <= current_max:
        find_count += 1
        if array[current_guess] == target:
            print(find_count)
            return True
        if array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_max + current_min) // 2 # 중간값을 계속 업데이트 해준다
    return  False # while문이 끝날때 까지 한번도 발견되지 않는다면




    return False


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)