def solution(people, limit):
    people.sort()  # 오름차순 정렬
    i, j = 0, len(people) - 1
    answer = 0
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # 가장 가벼운 사람 탑승
        j -= 1      # 가장 무거운 사람은 항상 탑승
        answer += 1
    return answer
