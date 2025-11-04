# 예외 처리가 관건인듯...
# 내풀이
```py
T = int(input())
for stage in range(1, T+1):
    do = list(input().split(" "))
    if do[-1] != '.':
        result = 'error'
        print(f"#{stage} {result}")
        continue
    stack = []
    for now in do:
        if now.isnumeric():
            stack.append(int(now))
        elif now == ".":
            if len(stack) < 1:
                result = 'error'
                break
            result = stack.pop()
        elif now in ["+", "-", "*", "/", "%", "**"]:
            if len(stack) < 2:
                result = 'error'
                break
            a = stack.pop()
            b = stack.pop()
            if now == "+":
                stack.append(int(a+b))
            elif now == "-":
                stack.append(int(a-b))
            elif now == "*":
                stack.append(int(a*b))
            elif now == "/":
                if b == 0:
                    result = 'error'
                    break
                stack.append(int(a/b))
            elif now == "%":
                if b == 0:
                    result = 'error'
                    break
                stack.append(int(a % b))
            elif now == "**":
                stack.append(int(a**b))
            else:
                result = 'error'
                break
        else:
            result = 'error'
            break
    print(f"#{stage} {result}")
```
=> 5개 오답

# GPT 피드백
### 뭐가 틀렸나?
1. split(" ")
- 여러 칸 공백이 들어오면 빈 토큰 ""이 생겨서 바로 error 납니다.
- 해결: 그냥 split() 쓰면 모든 공백을 정상 분할합니다.
2. 피연산자 순서 뒤집힘
- a = pop() (오른쪽), b = pop() (왼쪽)인데, 계산을 a-b, a/b로 해서 좌우가 바뀐 결과가 나와요.
- 해결: right = pop(), left = pop() 후 left op right로 계산.<br>
=> **이거 고치니깐 오답 갯수 1개로 줄었음..ㄹㅈㄷ..이걸 모르다니**
3. . 처리 조건
- 지금은 len(stack) < 1만 막고 있어요. 스택에 값이 2개 이상이어도 통과됩니다.
- 해결: .에서 스택 길이 == 1만 정답, 아니면 error.<br> => 이거 고치니깐 전체 정답
4. 숫자 판별
- isnumeric()는 음수(-3)를 숫자로 안 봅니다. (이 문제에 음수가 안 나온다면 큰 문제는 없지만)
- 해결: try: int(tok)로 파싱하는 방식이 견고합니다.
```py
T = int(input())
for stage in range(1, T+1):
    tokens = input().split()  # 공백 안전하게
    if not tokens or tokens[-1] != '.':
        print(f"#{stage} error")
        continue

    stack = []
    result = "error"

    for tok in tokens:
        if tok == '.':
            # 결과는 스택에 값이 '정확히 1개'여야 함
            result = str(stack.pop()) if len(stack) == 1 else "error"
            break

        elif tok in ['+', '-', '*', '/']:
            if len(stack) < 2:
                result = "error"
                break
            right = stack.pop()
            left  = stack.pop()

            if tok == '+':
                stack.append(left + right)
            elif tok == '-':
                stack.append(left - right)
            elif tok == '*':
                stack.append(left * right)
            elif tok == '/':
                if right == 0:
                    result = "error"
                    break
                stack.append(left // right)  # 항상 나누어떨어짐 → 정수 나눗셈

        else:
            # 숫자 파싱 (음수 대비)
            try:
                stack.append(int(tok))
            except ValueError:
                result = "error"
                break

    print(f"#{stage} {result}")
```
### 아니 근데 3번 조건은 어디서 확인???
- 문제는 “스택 길이 == 1” 조건을 직접 쓰진 않았지만, “정상적인 연산 결과 하나만 출력해야 한다”는 문장 구조상 필연적으로 그 조건이 필요합니다.