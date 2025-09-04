T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = input()  # 배열 입력

    lst = 0  # 연속한 1의 개수
    max_l = 0 # 연속한 1의 개수의 최대값
    for i in arr:
        if i == '1':   #arr 원소가 1이면
            lst += 1        # 길이에 1을 더한다
        else:               # 아니면
            lst = 0           # 연속하지 않으므로 0

        if lst > max_l:
            max_l = lst

    print(f'#{tc} {max_l}')
