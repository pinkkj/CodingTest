from functools import cmp_to_key

def solution(numbers):
    arr = list(map(str, numbers))

    def cmp(a, b):
        if a + b > b + a:  # a가 앞에
            return -1
        if a + b < b + a:  # b가 앞에
            return 1
        return 0

    arr.sort(key=cmp_to_key(cmp))
    ans = ''.join(arr)
    return '0' if ans[0] == '0' else ans