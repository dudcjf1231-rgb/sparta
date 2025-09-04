T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    s = []  # 스택을 하여 곱셈 결과의 모든 값들을 넣어본다.

    # 원소 앞이랑 뒤를 곱해서 증가하는 수여야 한다

    # 일단 나올 수 있는 arr[i] * aar[j] 의 값을 다 구해서 s에 넣어본다.
    for i in range(N):
        for j in range(i+1, N):  # 앞에서 i를 제외했기에 1개를 더 빼준다
            X = arr[i] * arr[j]  # 곱셈
            s.append(X)  # s 리스트에 더해준다.

    ans = -1
    #자리수를 비교하기 위해서는  N% 10을통해 할 수 있다.
    for x in s:      # 여기서까지 구상을 하였지만

                # 구상한 부분을 코드로 나타내기 어려워 밑에 부분은
        y = x       # 정답을 확인했습니다.
        prev = 10
        ok = True
        while y > 0:     # 정해지지 않은 반복문이다 보니까 while을 쓴다.
            d = y % 10      # 현재 가장 오른쪽 자리
            if d > prev:        # 왼쪽 자리(다음에 볼 자리)가 더 크다면,
                                    # 왼→오로 보면 감소가 생기므로 실패
                ok = False
                break
            prev = d
            y //= 10
        if ok and x > ans:
            ans = x

    print(f"#{tc} {ans}")