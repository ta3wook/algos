def solution(answers):
    answer = []
    
    # a = [1, 2, 3, 4, 5]
    # b = [2, 1, 2, 3, 2, 4, 2, 5]
    # c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a = list(range(1, 6))
    b = [x for i in [1, 3, 4, 5] for x in [2, i]]
    c = [x for i in [3, 1, 2, 4, 5] for x in [i, i]]
    
    patterns = [a, b, c]
    scores = [0] * 3
    
    for i, ans in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if ans == pattern[i % len(pattern)]:
                scores[j] += 1

    max_val = max(scores)
    answer = [i+1 for i, x in enumerate(scores) if x == max_val]
    
    answer.sort()
    return answer
