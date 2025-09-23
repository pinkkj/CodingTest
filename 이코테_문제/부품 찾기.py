import sys

N = input()
N_list = list(map(int, sys.stdin.readline().rstrip().split()))
M = input()
M_list = list(map(int, sys.stdin.readline().rstrip().split()))

N_list.sort()

def search(target, list):
    start = 0
    end = len(list) - 1
    while (start <= end):
        mid = (start+end) // 2
        if list[mid] > target:
            end = mid - 1
        elif list[mid] < target:
            start = mid + 1
        else:
            return mid
    return False

for target in M_list:
    if search(target, N_list) == False:
        print("no")
    else:
        print("yes")

# 이진 탐색 -> O((M+N) x logN)

# 계수 정렬을 이용한 식
n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')