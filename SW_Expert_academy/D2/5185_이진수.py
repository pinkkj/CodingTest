chr_to_num = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
T = int(input())
for test_case in range(T):
    result = ''
    len_of_num,num_16 = input().split()
    for i in range(len(num_16)):
        new = ''
        now = ''
        if num_16[i] in chr_to_num:
            now = int(chr_to_num[num_16[i]])
        else:
            now = int(num_16[i])
        
        use_1 = False
        if (now-1) % 2 == 0:
            use_1 = True
            now -= 1
        for n in range(3, 0, -1):
            if (now - 2**n) >= 0:
                now -= 2**n
                new += '1'
            else:
                new += '0'
        if use_1:
            new += '1'
        else:
            new += '0'
        result += new
    print(result)

# 다른 사람 풀이
T = int(input())
 
for test_case in range(1, T + 1):
    N, S = input().strip().split()
    N = int(N)
    answer = []
    for i in range(N):
        binary = f"{int(S[i],16):04b}"
        answer.append(binary)
    print(f"#{test_case} {''.join(answer)}")

# 포맷 지정자 :04b 해부
# b : 정수를 2진수로 출력.
# 4 : 최소 너비 4칸을 보장.
# 0 : 남는 자릿수는 0으로 채움(제로 패딩).
# (: 는 f-string에서 “포맷 시작”을 뜻하는 표식)