# n = int(input())

# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
#         if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
#             new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
#             if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
#                 error += 1  # error에 1씩 증가.
#     if error == 0:  
#         group_word += 1  # error가 0이면 그룹단어
# print(group_word)



# result = int(input()) # 그룹단어 테스트 케이스 입력

# for _ in range(result): # 테스트 케이스 만큼 반복문
#     word = input() # 단어입력
#     for i in range(1, len(word)): # 1부터 단어의 길이까지 반복문
#         if word.find(word[i-1]) > word.find(word[i]): # [h,a,p,p,y]
#             result -= 1
#             break
# print(result)


# >>> s = '가나다라 마바사아 자차카타 파하'
# >>> s.find('마')
# 5
# >>> s.find('가')
# 0
# >>> s.find('가',5)
# -1


N = int(input()) # 테스트 케이스

group = 0

for i in range(N):   
    Num = input() # 입력값 happy[p = 2]
    cnt = 0    
    for j in range(len(Num)-1): #입력값의 길이 -1 만큼 반복 
        if Num[j] != Num[j+1]: # 연속되는 단어가 같지 않다면 h != a // 뒤에 단어가 있어도 여기서 튕김
                Num_list = Num[j:] # a 다음 정렬               # 0:happy
                if Num_list.count(Num[j]) > 0: # 다음에 또 반복이 된다면? 있다면? // 다음 정렬에 몇번 등장하는지
                    cnt += 1 # 카운트 1 
                    
    if cnt == 0:
        group += 1 

print(group)      
        





# cnt = 0

# for i in range(int(input())):
#     word = input()
#     cnt+=list(word) == sorted(word, key=word.find)

# print(cnt)
