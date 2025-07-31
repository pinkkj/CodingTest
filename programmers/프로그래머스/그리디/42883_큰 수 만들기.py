def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        # 스택에 값이 있고, k > 0이며, 현재 숫자가 스택 top보다 크면 pop
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 아직 제거 횟수가 남았다면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    answer = ''.join(stack)
        
    return answer