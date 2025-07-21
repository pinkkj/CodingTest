initial_position = input()
result =0
# ex) a1
row = int(initial_position[1]) # 1
column = initial_position[0] # a
alpha_mapping = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
#위
if (row-2) > 0:
    #왼
    if (alpha_mapping[column] - 1) > 0:
        result = result + 1
    #오
    if (alpha_mapping[column] + 1) < 9:
        result = result + 1
#아래
if (row+2) < 9:
    #왼
    if (alpha_mapping[column] - 1) > 0:
        result = result + 1
    #오
    if (alpha_mapping[column] + 1) < 9:
        result = result + 1 
#왼
if (alpha_mapping[column] - 2) > 0:
    #위
    if (row-1) > 0:
        result = result + 1
    #아래
    if (row+1) < 9:
        result = result + 1 
#오
if (alpha_mapping[column] + 2) < 9:
    #위
    if (row-1) > 0:
        result = result + 1
    #아래
    if (row+1) < 9:
        result = result + 1 

print(result)

# 교정

# # 입력 예: "a1"
# position = input()

# # 열을 숫자로 변환 (a=1, b=2, ..., h=8)
# col = ord(position[0]) - ord('a') + 1
# row = int(position[1])

# # 나이트가 이동할 수 있는 8가지 방향 (dy, dx)
# moves = [
#     (-2, -1), (-2, 1), (2, -1), (2, 1),
#     (-1, -2), (-1, 2), (1, -2), (1, 2)
# ]

# count = 0
# for dy, dx in moves:
#     new_row = row + dy
#     new_col = col + dx
#     if 1 <= new_row <= 8 and 1 <= new_col <= 8:
#         count += 1

# print(count)
