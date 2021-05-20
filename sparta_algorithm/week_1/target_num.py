numbers = [2,3,1]
target_number = 0

# 1. +2 +3 +1 = 6 +++
# 2. +2 +3 -1 = 4 ++-
# 3. +2 -3 +1 = 0 #타겟 +-+
# 4. +2 -3 -1 = -2 +--
# 5. -2 +3 -1 = 2
# 6. -2 +3 -1 = 0 # 타겟
# 7. -2 -3 +1 = -4
# 8. -2 -3 -1 = -7

def plus_minus(array,)


#n의 길이의 배열에서 더하거나 뺀 모든 경우의 수는 n-1 의 길이의 배열에서 마지막 원소를 더하거나 뺀 경우의 수를 추가하면된다
def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    if sum(numbers) > target_number:
        sum(numbers) = sum(numbers) - 1
    else:
        return

    if sum(numbers) == target_number:

      return target_number


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
