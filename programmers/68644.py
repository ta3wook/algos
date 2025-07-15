def solution(numbers):
    answer = []
    num = len(numbers)
    for i in range(0, num-1):
        for j in range(i+1, num):
            answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    answer.sort()
    return answer
