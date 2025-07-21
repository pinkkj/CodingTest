N, M = map(int, input().split())
a, b ,d =map(int, input().split())
current_position = (a,b)
# 육지, 바다 (0:육지, 1:바다)
arr = []
for i in range(M):
    land_sea = list(map(int, input().split()))
    arr.append(land_sea)

move = [(-1,0),(0,-1), (1,0), (0,1)]
result = 1
end = False
exist = False
while(not end):
    exist = False
    future_d = d
    for _ in range(4):
        future_d = future_d + 1
        if (future_d > 3):
            future_d = future_d - 4
        future_a=a+move[future_d][0]
        future_b=b+move[future_d][1]
        future_position = arr[future_a][future_b]
        if (future_position != 1):
            a = a+move[future_d][0]
            b = b+move[future_d][1]
            arr[a][b] = 1
            d = future_d
            result = result+1
            exist = True
            break

    if (not exist):
        a = a - move[d][0] 
        b = b - move[d][1]
        d = d + 1
        if (d == 4):
            d = 0
        if (arr[a][b] == 1):
            end = True

print(result)

# 개선할 사항
# 항목	                    평가	                               개선방향
# ✔ 전체 구조	기본 로직은 정확하게 동작	                     가독성과 효율성을 위해 visited 배열 분리 추천
# ⚠ 방향 처리	회전, 후진 로직이 다소 혼란스럽게 작성됨	      turn_left() 함수 등으로 추상화 가능
# ⚠ 방문 처리	arr 자체에 방문 여부를 표시	                     원본 맵과 방문여부 분리가 더 명확함
# ⚠ 하드코딩	방향 회전 관련 코드가 중복	                     direction 배열과 함수 활용 가능
