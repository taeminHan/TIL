def solution(A):
    answer = 1

    for i in sorted(A):
        if answer == i:
            answer += 1

    return answer
# https://app.codility.com/demo/results/trainingYMR96N-PD8/
print(solution([1,3,6,4,1,2]))