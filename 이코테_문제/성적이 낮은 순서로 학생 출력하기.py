num = int(input())

array = []
for i in range(num):
    name, score = input().split(" ")
    array.append([name, score])

def setting(s):
    return s[1]

result = sorted(array, key=setting)
for name, _ in result:
    print(name, end=' ')