# n은 몇번막대에서 몇번 막대로 옮길거야!

def hanoi_tower(n, start, end) : # n개의 원판을 몇번막대에서 몇번막대로 옮길거야
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계 n-1개의 원판을 2번 막대로 
    print(start, end) # 2단계 start에서 end막대로 // 제일밑큰 원판을 옮긴다
    hanoi_tower(n-1, 6-start-end, end) # 3단계 1번단계와 마찬가지로 작동
    
n = int(input())

print(2**n-1)

hanoi_tower(n, 1, 3) # n개의 원판을 1번에서 3번으로 전부 옮기기
 
