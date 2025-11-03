T = int(input())
for stage in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    what_first = M % N
    print(f"#{stage} {numbers[what_first]}")