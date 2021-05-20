people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# # def check_adult(person):
# #     if person['age'] > 20:
# #         return "성인"
# #     else:
# #         return '청소년'

# # result = map(check_adult, people) #map을 써서 people을 하나하나 돌면서 체크 어덜트에다 넣어라 

# # print(list(result))


# # if 문 짧게 써보자
# def check_adult(person):
#     return ('성인' if person['age'] > 20 else '청소년')

# result = map(check_adult, people) #map을 써서 people을 하나하나 돌면서 체크 어덜트에다 넣어라 

# result = map(lambda x: x, people) # result = map(lambda person: person, people)이랑 같은 뜻
# print(list(result))

# #음... 한줄짜리 함수를 굳이 만들지 말고 이렇게 람다로 써라?

# result = map(lambda person: ('성인' if person['age'] > 20 else '청소년'), people)

# # person은 계속 돌면서 출력되는데 거기에 삼항연산자 조건을 돌아서 리턴해라

#필터 map과 매우유사한데 true 값만 가져온다

result = filter(lambda person:person['age'] > 20, people)
# person['age']값이 20보다 큰애들만 담아라

print(list(result))

