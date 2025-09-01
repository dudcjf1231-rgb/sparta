T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = []


    for _ in range(N):
        a, b, c = map(int, input().split())
        total = 0.35*a + 0.45*b + 0.2*c
        score.append(total)

    
    # K번째 학생의 총점 - 0번부터 인덱스 시작이므로 k-1을 해줘야 K번째 사람이 된다.
    target = score[K-1] 
    higher = 0
    for s in score:
        if s > target:   #k번째보다 높은 사람 수 카운트
            higher += 1         #이렇게 하면 정렬을 하지 않더라도 k가 몇번째인 줄 알 수 있따. 

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    block = N//10

    grade_s = higher//block

    answer = score[grade_s]

    print(f'#{tc} {answer}')