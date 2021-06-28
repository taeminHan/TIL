def solution(array, commands):
    answer = []

    for i in commands:
        # i에는 [2, 5, 3]이 먼저 들어 갑니다. example 기준!
        slicedArray = array[int(i[0])-1:int(i[1])]
        # array에서 i[0]번째 숫자부터 i[1]번째 숫자까지 자르고
        sorted_slicedArray = sorted(slicedArray)
        # 위에서 자른 array를 정렬을 해줍니다!

        answer.append(sorted_slicedArray[int(i[2])-1])
        # 그리고 슬라이스와 정렬을 거쳐나온 sorted_slicedArray에서 i[2]번째 수를 answer에 append하기

        # 위 슬라이스나 append할때 -1을 했냐면 문제에서 말하는 
        # K번째 숫자들은 0부터 시작이 아닌 1부터 시작이기 때문이다.
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))