numbers = list(range(1,10_001))
remove_list = [] # 삭제할 숫자 리스트

for num in numbers:
    for n in str(num): # 넘버스의 숫자를 받고 또 그 숫자를 스트링 형태로 반복한다
        num += int(n) #생성자가 있는 숫자 
    if num <= 10_000:
        remove_list.append(num)

for remove_num in set(remove_list): # set으로 중복값제거
    number.remove(remove_num)
for self_num in numbers:
    print(self_num)
