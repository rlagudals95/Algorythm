N = int(input())  # 과목수

test_list = list(map(int, input().split()))  # 시험 점수 리스트
max_score = max(test_list)  # 테스트 리스트의 가장 큰값

new_list = []  # 새로운 어레이를 만들어야 한다
for score in test_list:
    new_list.append(score / max_score * 100)
    test_avg = sum(new_list) / N  # sum 함수는 모두 더해주는 함수
print(test_avg)

