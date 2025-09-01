#10개의 수를 입력 받아, 그 중에서 홀수만 더한 값 출력

T = int(input())

for tc in range(1, T+1): # 테스트 케이스 
    arr = list(map(int, input().split())) # 10개 수를 입력 받을 배열

    s = 0  # i가 홀수면 더할 변수
    for i in arr:
    # 만약 홀수 일 경우?
        if i % 2 == 1: # i를 2로 나눈 나머지가 1이면 홀수이다.
            s += i     # 홀수니까 i를 더한다
   

    print(f'#{tc} {s}')

