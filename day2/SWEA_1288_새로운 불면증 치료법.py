T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input())

    visited = [0] * 10    # 숫자를 이미 셌는지 확인
    cnt = 0             # 숫자가 있을때마다 카운트
    k = 0    # 0~9까지 없을때마다 N에 k를 곱해줄  초기값

    while cnt < 10:
        k += 1      # 카운트 1  증가
        cur = N * k

        # 문자열 변환 없이 자리수 추출
        while cur > 0:
            d = cur % 10   # 자리수 확인 하는 방법 10으로 나눠주고 나머지가 자리수를 확인할 수 있다.
            if not visited[d]:  # 나머지가 이미 셌던 숫자에 없었으면
                visited[d] = 1  # 1로 표시해 셌던건지 확인
                cnt += 1        # 그리고 횟수를 증가 시키다.
                if cnt == 10:   # 만약 횟수가 10이 됐다면 0~9까지 다나온거라 멈춘다
                    break
            cur //= 10  #다음 자리 수를 확인할 수 있게 10으로 나눠준다.

    print(f"#{tc} {k*N}")




