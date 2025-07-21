def solution(n, lost, reserve):
    answer = 0
    # 가지고 있는 체육복 수 세기
    how_many_cloth_have = {}
    for num in range(1, n+1):
        cloth = 1
        if (num in lost):
            cloth = cloth - 1
        if (num in reserve):
            cloth = cloth + 1
        how_many_cloth_have[num] = cloth
    # 체육복 빌리기
    for num in range(1, n+1):
        # 빌려야하는 상황
        if (how_many_cloth_have[num] == 0):
            if (((num-1) > 0) and (how_many_cloth_have[num-1]==2)):
                how_many_cloth_have[num-1] = 1
                how_many_cloth_have[num] = 1
            else:
                if (((num+1) < n+1) and (how_many_cloth_have[num+1] == 2)):
                    how_many_cloth_have[num+1] = 1
                    how_many_cloth_have[num] = 1
    # 몇 명이 체육복을 가질까?
    for num in range(1, n+1):
        if (how_many_cloth_have[num] >0):
            answer = answer + 1
    
    return answer
