from collections import deque
def solution(maps):
    answer = 0
    col_len = len(maps[0])
    raw_len = len(maps)
    
    def move(now_x, now_y,d, step):
                next_x,next_y = now_x+d[0], now_y+d[1]
                if (0<=next_y<len(maps)) and (0<=next_x<len(maps[0])):
                    if maps[next_y][next_x] == 1:
                        queue.append((next_x,next_y,step+1))
                        maps[next_y][next_x] = 0
    
    d_list = [[0,1],[0,-1],[1,0],[-1,0]]
    queue = deque([(0,0,1)])
    maps[0][0]=0
    while queue:
        x,y,step = queue.popleft()
        if (x == (col_len-1)) and (y == (raw_len - 1)):
                answer = step
                break
        for d in d_list:
            move(x,y,d,step)
    if (answer == 0):
        answer = -1
    return answer