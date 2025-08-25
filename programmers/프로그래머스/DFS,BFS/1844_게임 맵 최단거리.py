from collections import deque
def solution(maps):
    answer = 0
    raw_len = len(maps[0])
    col_len = len(maps)
    if (maps[raw_len-2][col_len-2] == 0) and (maps[raw_len-1][col_len-2] == 0) and (maps[raw_len-2][col_len-1] == 0):
        return -1
    
    def move(now_x, now_y,where,d, step):
                if (where == "dx"):
                    next_x = now_x + d
                    next_y = now_y
                else:
                    next_y = now_y + d
                    next_x = now_x
                if (0<=next_y<len(maps[0])) and (0<=next_x<len(maps)):
                    if maps[next_y][next_x] == 1:
                        queue.append((next_x,next_y,step+1))
                        maps[next_y][next_x] = 0
    
    dx_list = [-1,1]
    dy_list = [-1,1]
    queue = deque([(0,0,1)])
    maps[0][0]=0
    while queue:
        x,y,step = queue.popleft()
        if (x == (col_len-1)) and (y == (raw_len - 1)):
                answer = step
                break
        for dy in dy_list:
            move(x,y,"dy",dy,step)
        for dx in dx_list:
            move(x,y,"dx",dx,step)
    return answer
