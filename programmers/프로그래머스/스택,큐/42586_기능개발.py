def solution(progresses, speeds):
    answer = []
    stack = []
    n = 0
    for i in range(len(speeds)):
        # 얼마나 걸리나?
        if ((100-progresses[i]) % speeds[i]) != 0:
            time = ((100-progresses[i]) // speeds[i]) + 1
        else:
            time = (100-progresses[i]) // speeds[i]
            
        # 세기
        if ((len(stack) == 0)or (stack[0] >= time)):
            n = n + 1
            stack.append(time)
        else:
            answer.append(n)
            while (len(stack) != 0):
                stack.pop()
            print(stack)
            stack.append(time)
            n = 1
    answer.append(n)
    return answer