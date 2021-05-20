n=int(input())
nums=[]

for _ in range(n): # 출력할 만큼 범위지정
    count = int(input()) # 출력할 숫자 입력
    nums.append(count) # 빈정렬에 차곡차곡 넣어준다

for i in sorted(nums): # 내림순으로 들어갔던 것 오름차순으로 정렬 
    print(i)           # 반복문으로 돌리면서 출력