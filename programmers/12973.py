def solution(s):
    stack = []
    for w in s:
        if stack:
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        else:
            stack.append(w)
    
    if not stack:
        answer = 1
    else:
        answer = 0
    
    return answer
