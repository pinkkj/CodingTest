def solution(numbers, target):
    answer = 0
    stack = [[-numbers[0],0],[numbers[0],0]]
    while stack:
        out = stack.pop()
        value = out[0]
        index = out[1]
        
        if ((index == len(numbers) - 1)):
            if (value == target):
                answer = answer + 1
        else:
            index = index + 1
            stack.append([value-numbers[index], index])
            stack.append([value+numbers[index], index])
    return answer