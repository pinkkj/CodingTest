list_num = int(input())
list = []
for i in range(list_num):
    list.append(int(input()))

list.sort()
list.reverse()
for i in list:
    print(i, end=" ")