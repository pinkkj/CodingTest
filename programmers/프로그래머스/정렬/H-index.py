def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for i in range(citations[0],0,-1):
        n = 0
        for num in citations:
            if num >= i:
                n = n + 1
            else:
                break
        if i <= n:
            answer = i
            break
    
            
    return answer


# 다른 풀이 1
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

# ✅ 왜 이렇게 동작하나?

# H-Index 정의: h편 이상의 논문이 각각 h번 이상 인용된 경우, 그 중 최대값 h가 H-Index

# 여기서 (순번, 인용 수)를 비교할 때 둘 중 작은 값이 실제로 만족 가능한 H 값이 됩니다.

# 마지막으로 그 중 최댓값을 고르면 H-Index가 됩니다.

# 다른 풀이 2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0