T = int(input())


def bus_move(k, n, stop):
    last = 0  # 마지막 충전 위치
    bus = k  # 현재 버스가 갈 수 있는 최대 위치
    cnt = 0  # 충전 횟수

    while bus < n:  # 아직 도착지점(n)에 도착하지 못했다면
        # 뒤로 가면서 충전소 찾기
        while bus > last and stop[bus] == 0:  # 현재 위치에 충전소가 없으면 한 칸씩 뒤로 이동
            bus -= 1

        if bus == last:  # 충전이 불가능하다면
            return 0

      #충전에 성공했으면
        last = bus  # 위치 갱신
        cnt += 1  # 충전 횟수 +1
        bus += k  # 충전했으니 다시 k만큼 전진

    return cnt  # 도착지에 도달했을 때
                # 충전 횟수 카운트


for tc in range(1, T + 1):
    k, n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    stop = [0] * (n + 1)  # 정류소 리스트

    for i in arr:  # 충전기가 있는 정류장은
        stop[i] = 1  # 1로 표시

    result = bus_move(k, n, stop)
    print(f"#{tc} {result}")





