T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input())) for _ in range(N)]

    # 이익
    money = 0

    # 농장의 정중앙과 거리 차이가 d 이하인 곳만 수확할수 있다.


    # 거리 d는 농장의 한 변의 길이 // 2
    d = N // 2

    # 정 중앙의 좌표
    center = (d, d)

    # 모든 위치 (i,j) 에서 정중앙까지 이동하는데 가로로 이동한 횟수 x, 세로로 이동한 횟수 y
    # x + y <= d 이하인 곳들의 합을 구한다.

    for i in range(N):
        for j in range(N):
            # 거리 계산
            if abs(j-d) + abs(j-d) <= d:
                money += matrix[i][j]

    print(f"#{tc} {money}")



'''
초기 생각한 버전
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split()))for _ in range(N)]

    # 농장의 크기는 항상 홀수 이다
    # 혹시 전체 정사각형의 크기에서 나머지를 빼면 어떨까

    s = 0
    for i in range(N):
        for j in range(N):
          s += matrix[i][j] #전체 정사각형 합
          
          여기서 나머지부분을 빼는 법을 아무리 생각해도 나오지않아서 막혔습니다/. 
'''

