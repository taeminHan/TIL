def solution(A, B, K):
    if A % K == 0:
        return (B//K)- (A//K) + 1
    else:
        return (B//K)- (A//K)

print(solution(11, 345, 17))

#https://app.codility.com/demo/results/trainingQ383P8-BBD/