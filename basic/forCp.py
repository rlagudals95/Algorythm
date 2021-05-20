# 일반적인 for문출력

nums = []

for x in range(1, 11): 
    nums.append(x)

# comprehension한 for문 한줄로 코드를 줄일 수 있다

nums = [x for x in range(1,11)]

# 1~ 10 제곱 값으로 이뤄진 한줄 for문

nums2 = [x*x for x in range(1,11) ]

# 두개의 for문을 한줄로 표현

for dan in range(2,10): # 2 ~ 9
    for i in range(1,10): # 1 ~ 9
        print(f'{dan} x {i} = {dan*i}')

# 이제 한줄로!

[print(f'{dan} x {i} = {dan*i}') for dan in range(2,10) for i in range(1,10)]