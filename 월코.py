def solution(absolutes, signs):
    result = []
    for i in range(len(absolutes)):
        if signs[i]:
            result.append(absolutes[i])
        else:
            result.append(-absolutes[i])
    print(sum(result))


solution([4, 7, 12], [True, False, True])
