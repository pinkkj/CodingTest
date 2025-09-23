import sys

N, M = map(int, input().split())
rice_hight = list(map(int, sys.stdin.readline().rstrip().split()))

rice_hight.sort()

limit = rice_hight[-1]
flag = True
while flag:
    result = 0
    for i in range(len(rice_hight)-1, -1, -1):
        if rice_hight[i] <= limit:
            break
        else:
            result = result + (rice_hight[i] - limit)
            if result == M:
                flag = False
                print(limit)
                break
    limit = limit - 1