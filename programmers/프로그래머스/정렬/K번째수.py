# 내풀이
def solution(array, commands):
    answer = []
    for command in commands:
        new=array[command[0]-1:command[1]]
        new.sort()
        answer.append(new[command[2]-1])
    return answer

#다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

def solution(array, commands):

    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]