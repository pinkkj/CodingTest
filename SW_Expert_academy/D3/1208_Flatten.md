# 내 코드
```py
for stage in range(1, 11):
    N = int(input())
    dumps = list(map(int, input().split()))
    for _ in range(N):
        dumps[dumps.index(max(dumps))] -= 1
        dumps[dumps.index(min(dumps))] += 1
    print(f"#{stage} {max(dumps) - min(dumps)}")
```
# GPT 피드백
## 비효율적인 부분 (그래도 통과는 함)
```py
dumps[dumps.index(max(dumps))] -= 1
dumps[dumps.index(min(dumps))] += 1
```
여기서 매 덤프마다
- max(dumps) (한 번 순회)
- dumps.index(max(dumps)) (다시 순회)
- min(dumps) (또 순회)
- dumps.index(min(dumps)) (또 순회)

이렇게 리스트 전체를 여러 번 도는 구조라서,
시간 복잡도 기준으로 보면 덤프 횟수 × 리스트 길이 × 상수만큼 계속 돎.

## 살짝 더 깔끔한 버전
최소/최대값을 한 번만 계산해서 쓰고,
이미 평탄화된 경우(max-min <= 1)는 바로 끊어주는 버전:
```py
for stage in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(dump):
        max_h = max(boxes)
        min_h = min(boxes)
        # 이미 차이가 1 이하면 더 해봐야 의미 없음
        if max_h - min_h <= 1:
            break

        max_idx = boxes.index(max_h)
        min_idx = boxes.index(min_h)

        boxes[max_idx] -= 1
        boxes[min_idx] += 1

    print(f"#{stage} {max(boxes) - min(boxes)}")
```
## 고급 버전 아이디어 (나중에 도전용)
이 문제는 높이가 0~100 사이이기 때문에,
리스트 자체를 정렬하거나 카운팅 배열(크기 101)를 써서
최댓값/최솟값을 빠르게 관리하는 풀이도 자주 쓰여.

지금은 이 정도면 충분히 잘 짠 코드라서,
다음 단계로 효율성까지 신경 쓰고 싶을 때 카운팅 방식도 한 번 도전해봐도 좋아.\

```py
for tc in range(1, 11):      # 테스트 케이스는 항상 10개
    dump = int(input())      # 덤프 횟수
    heights = list(map(int, input().split()))

    # 0~100 높이에 대한 카운팅 배열
    counts = [0] * 101
    for h in heights:
        counts[h] += 1

    # 현재 최소/최대 높이 찾기
    min_h = 0
    while counts[min_h] == 0:
        min_h += 1

    max_h = 100
    while counts[max_h] == 0:
        max_h -= 1

    # 덤프 수행
    for _ in range(dump):
        # 이미 평탄화가 거의 끝난 경우
        if max_h - min_h <= 1:
            break

        # 가장 높은 곳에서 한 칸 빼기
        counts[max_h] -= 1
        counts[max_h - 1] += 1

        # 가장 낮은 곳에서 한 칸 올리기
        counts[min_h] -= 1
        counts[min_h + 1] += 1

        # max_h, min_h 갱신
        while max_h > 0 and counts[max_h] == 0:
            max_h -= 1
        while min_h < 100 and counts[min_h] == 0:
            min_h += 1

    print(f"#{tc} {max_h - min_h}")
```