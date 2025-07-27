def solution(name):
    min_move = len(name)-1
    answer = 0
    # 맨끝부터 연속적인 A가 있을때
    while (name[min_move] == 'A'):
        min_move = min_move - 1
    if (min_move < 0):
        return 0
    
    # for문으로 돌기
    for i, char in enumerate(name):
        answer = answer + min(ord(char)-ord('A'), ord('Z') - ord(char) + 1)
        end_of_A = i + 1
        while (end_of_A < len(name) and name[end_of_A] == 'A'):
            end_of_A = end_of_A + 1
        min_move = min(min_move, 2 * i + len(name) - end_of_A, 2*(len(name)- 1) + i)
    answer = answer + min_move
    return answer

print(solution("JAN"))