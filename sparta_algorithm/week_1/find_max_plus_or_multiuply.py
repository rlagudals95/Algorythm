input = [0, 3, 5, 6, 1, 2, 4]

def find_max(array):
    multiply_sum  = 0 # 현재 계산 합계
    for number in array:
        if number <= 1 or multiply_sum <= 1: # 1보다 작거나 같거나 혹은 모두 더해진 함계가 1보다
            multiply_sum += number
        else:
            multiply_sum *= number




result = find_max(input)
print(result)