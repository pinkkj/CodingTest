N = int(input())
result = []
sen = []
for _ in range(N):
    sen.append(input())
start = 0
end = -1
while True:
    if (start-N) == end:
        result.append(sen[start])
        break

    if sen[start] > sen[end]:
        result.append(sen[end])
        end -= 1
    elif sen[start] < sen[end]:
        result.append(sen[start])
        start += 1
    else:
        tmp_start = start
        tmp_end = end
        no_problem = False
        while sen[tmp_start] == sen[tmp_end]:
            tmp_start += 1
            tmp_end -= 1
            if (tmp_start-N) == tmp_end:
                no_problem = True
                break
        if no_problem:
            result.append(sen[start])
            start += 1
        else:
            if sen[tmp_start] > sen[tmp_end]:
                result.append(sen[end])
                end -= 1
            elif sen[tmp_start] < sen[tmp_end]:
                result.append(sen[start])
                start += 1

    if len(result) % 80 == 0:
        result.append("\n")
print("".join(result))