def solution(a, edges):
    answer = 0
    if sum(a) == 0:
        if a == [0] * len(a):
            answer = 0
        else:
            for i in range(len(a)):
                try:
                    answer += abs(max(abs(a[i]), abs(a[i + 1])) - min(abs(a[i]), abs(a[i + 1])))
                except:
                    pass
    else:
        answer = -1
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
