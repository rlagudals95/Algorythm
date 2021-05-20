#이진탐색 혹은 이분탐색이라고 한다

# 장점 빠르고 실제로 쓰인다
# 단점 정렬이 되있어야 하고 만들기 까다롭다?

#중간의 인덱스 값을 구한다 (약간 업앤 다운게임?)
#10억개 9억 6천과 현재 중간값 
#0-------5----9.6---10
#5------10 >> 7.5------10 >>>>>> 8.75----10 이렇게 범위를 줄여나가는 것

#중간값이 찾는 수보다 클때는
#0----4.6---5-------10
#0--------4.6----5 범위를 뒤에서 컷! start= 0그대로 end = 미드인덱스 -1

arr = [1,2,3,5,6,7,8,9,10,11]

def search(arr, targetNum):
    start = 0
    end = len(arr) - 1
    while(start <= end): #엔드랑 스타트가 같거나 클때 값이 나오지않을까?
        
        # midIndex = len(arr) // 2 # 어레이를 반으로 나눈값은 5 //이거쓰면 무한루프임 대신에 밑에
        midIndex = (start + end) // 2 # 이게 중간값이 나옴 계속 5가 나오지 않음
        indexValue = arr[midIndex] # 그리고 중간값은 7 (7을기준으로 좌우로 나뉨)
        
        if indexValue == targetNum:
            return midIndex # 찾았을때 미드인덱스 리턴
        elif indexValue < targetNum:
            start = midIndex + 1
        elif indexValue > targetNum: #중간값이 타겟 넘버보다 큰 경우
            end = midIndex - 1 # 미드 인덱스 까지 검사를 했기 때문에 -1


        print("start:",start, "end:", end)
    return -1

# 1------5-----8---11 8을 찾고싶다
# 5---------11 스타트가 5로 좁혀졌다 엔드는 그대로
print(search(arr, 4)) ##  값은 6이 나오는데 8이라는 숫자는 6번째 인덱스임