# 내풀이
```py
T = int(input())

def find_leaf(N, tree):
    if tree[0][N] != 0 and tree[1][N] != 0:
        return 1 + find_leaf(tree[0][N], tree) + find_leaf(tree[1][N], tree)
    # 실수할뻔.. return 되면 그 함수는 끝! 만약 리스노드가 꽉차있는데 이 if문이 없으면, 나머지 한쪽에 대해서는 안봄
    if tree[0][N] != 0:
        return 1 + find_leaf(tree[0][N], tree)
    if tree[1][N] != 0:
        return 1 + find_leaf(tree[1][N], tree)
    return 1

for stage in range(1, T+1):
    result = 0
    E, N = map(int, input().split())
    number_node = E + 1
    tree = [[0 for i in range(number_node + 1)] for _ in range(2)]
    info_list = list(map(int, input().split()))
    for i in range(0,len(info_list),2):
        root = info_list[i]
        leaf = info_list[i+1]
        if tree[0][root] == 0:
            tree[0][root] = leaf
        else:
            tree[1][root] = leaf
    
    result = find_leaf(N,tree)
    print(f"#{stage} {result}")
```
# GPT 조언
## 재귀
```py
import sys

T = int(sys.stdin.readline())

def count_subtree(u, tree):
    if u == 0:
        return 0
    left = tree[0][u]
    right = tree[1][u]
    count = 1  # 자기 자신
    if left:
        count += count_subtree(left, tree)
    if right:
        count += count_subtree(right, tree)
    return count

for tc in range(1, T + 1):
    E, N = map(int, sys.stdin.readline().split())
    info_list = list(map(int, sys.stdin.readline().split()))

    # 더 안전한 크기 산정 (SWEA 기본 규격만 믿을 거면 E+1 유지해도 OK)
    number_node = max(info_list)  # 또는: number_node = E + 1
    tree = [[0] * (number_node + 1) for _ in range(2)]  # [left[], right[]]

    for i in range(0, len(info_list), 2):
        parent = info_list[i]
        child = info_list[i + 1]
        if tree[0][parent] == 0:
            tree[0][parent] = child
        else:
            tree[1][parent] = child

    ans = count_subtree(N, tree) if N <= number_node else 0
    print(f"#{tc} {ans}")
```
## 재귀X -> stack 이용
```py
import sys

T = int(sys.stdin.readline())

def count_subtree_iter(start, tree):
    if start == 0:
        return 0
    stack = [start]
    cnt = 0
    while stack:
        u = stack.pop()
        if u == 0:
            continue
        cnt += 1
        left = tree[0][u]
        right = tree[1][u]
        if left:
            stack.append(left)
        if right:
            stack.append(right)
    return cnt

for tc in range(1, T + 1):
    E, N = map(int, sys.stdin.readline().split())
    info_list = list(map(int, sys.stdin.readline().split()))

    number_node = max(info_list)  # 또는 E + 1
    tree = [[0] * (number_node + 1) for _ in range(2)]

    for i in range(0, len(info_list), 2):
        parent = info_list[i]
        child = info_list[i + 1]
        if tree[0][parent] == 0:
            tree[0][parent] = child
        else:
            tree[1][parent] = child

    ans = count_subtree_iter(N, tree) if N <= number_node else 0
    print(f"#{tc} {ans}")
```