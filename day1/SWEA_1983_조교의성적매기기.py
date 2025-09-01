T = int(input())

for tc in range(1, T+1): # 테스트케이스
    N, K = map(int, input().split())  #N은 학생수, K는 알고 싶은 번호
    score = []

    for _ in range(N):   #N명의 숫자를 반복해서 성적을 입력 받는다.
        a, b, c = map(int, input().split()) # a: 중간고사, b: 기말고사 c: 과제
        total = (0.35 * a) + (0.45 * b) + (0.2 * c)
        score.append(total)


    # 여기서 부터 막혔습니다. 30분째 고민 나오지 않아 참고했습니다.
    target = score[K - 1]  # K번째 학생의 총점 - 0번부터 인덱스 시작이므로 k-1을 해줘야 K번째 사람이 된다.
    higher = 0
    for s in score:        # K번째보다 높은 사람 수 카운트
        if s > target:     # 이렇게 하면 정렬을 따로 하지않아도 K가 몇번째인지 알 수 있다.
            higher += 1

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    block = N // 10                 # 각 평점에 해당하는 인원 수 # 만약 N이 20명이면
                                    # 인원수는 20명이 된다.
    grade_idx = higher // block     # 높은 사람 수에 따른 평점 구간(0~9)
    answer = grade[grade_idx]

    print(f"#{tc} {answer}")


