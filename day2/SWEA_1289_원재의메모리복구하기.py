
T = int(input())

for tc in range(1, T+ 1):
    arr = list(input())

    # 길이는 따로 변수에 저장해두는게 좋다.
    n = len(arr)

    # 앞에서 차례로 바꿀 메모리
    change_arr = ["0"] * n

    cnt = 0


    for i in range(n):
        ith_char = arr[i]
        # 원래 메모리의 i번째 글자와 현재 내가 바꾸고 있는 메모리의 i번째 글자가 다르면 바꾼다.
        if ith_char != change_arr[i]:
            # i 번째 비트를 바꿨다면 끝까지 비트를 다 바꿔줘야한다.
            # 비트 변환시 1증가
            cnt += 1
            for j in range(i, n):
                # 반복문을 하나 더 사용 i <= j < n 일때 j 번째 글자도 모두 변경한다.
                change_arr[j] = ith_char

        if change_arr == arr:
           # 비트 바꾼 배열이랑 원래 배열이 같으면 그만한다.
            break

    print(f"#{tc} {cnt}")

'''
초기 구상
T = int(input())

for tc in range(1, T+1):
    arr = input()

    # 초기값으로 돌아가게 되고 모든 bit가 0
    # 인덱스를 선택하면 끝까지 바뀐다.
    # 주어진 배열과 똑같이 될려면 몇번을 돌려야 하는가
    # 정해진 반복이 아니니까 while을 써야하지않을까?
    
    # 비트 변환시 cnt를 1씩 증가
'''




