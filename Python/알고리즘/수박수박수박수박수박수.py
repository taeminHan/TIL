def solution(n):
    word = '수박'
    if n % 2 == 0:
        count = int(n / 2)
        answer = word * count

    else:
        count = int((n - 1) / 2)
        answer = word * count + '수'
    return answer
