from collections import deque
def solution(n, computers):
    check_list = [False] * n
    queue = deque()
    answer = 0 
    
    def bfs(now_com_index):
        computers[now_com_index][now_com_index] += 1
        for i in range(len(computers[now_com_index])):
            if computers[now_com_index][i] == 1:
                       queue.append(i)
                       computers[now_com_index][i] += 1
                       check_list[i] = True
        while queue:
            link_com = queue.popleft()
            bfs(link_com)
                
    for i in range(len(check_list)):
                       if check_list[i] == False:
                            bfs(i)
                            check_list[i] = True
                            answer = answer + 1
    return answer