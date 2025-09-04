T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = 1    # 당근 개수가 증가하는 지점의 길이
    max_v = 1  # 당근이 증가하지 않아도 최소 1이라해서 최대값을 1로 설정

    for i in range(N - 1):
        if arr[i + 1] > arr[i]: #만약 다음 인덱스 원소가 현재 인덱스보다 크다면
            lst += 1      # 길이가 1이 늘어난다.
        else:           # 증가하지 않는다면
            lst = 1     # 길이는 1이다

        if lst > max_v:   #길이가 최대값보다 길다면
            max_v = lst    # 최대값은 lst가 된다

    print(f'#{tc} {max_v}')
