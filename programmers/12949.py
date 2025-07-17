def solution(arr1, arr2):
    answer = []

    for m in range(len(arr1)):
        tmp1 = []
        for r in range(len(arr2[0])):
            tmp2 = 0
            for n in range(len(arr1[0])):
                tmp2 += arr1[m][n] * arr2[n][r]
            tmp1.append(tmp2)
        answer.append(tmp1)
        
    return answer
