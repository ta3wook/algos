def solution(food):
    answer = ''
    
    processed = []
    for num in food:
        processed.append(num // 2)
    
    for i, num in enumerate(processed):
        for _ in range(num):
            answer += str(i)
    
    answer = answer + '0' + answer[::-1]
    
    return answer
