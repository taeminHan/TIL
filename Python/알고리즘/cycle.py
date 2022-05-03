def solution(A, K):
    if(len(A) == 0):
        pass
    else:
        for i in range(K):
            A.insert(0, A.pop(-1))
    return A


https://app.codility.com/demo/results/training87E95W-AXS/