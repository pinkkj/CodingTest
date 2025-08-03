def solution(s):
    stack = []
    if (s[0] == ')'):
        return False
    else:
        stack.append(s[0])
        
    for i in s[1:]:
        if (i==')') and (stack):
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        return False    

    return True