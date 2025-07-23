def solution(s):
    answer = True
    
    stack = []
    for b in s:
        if stack:
            if b == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
        else:
            stack.append(b)

    if stack:
        answer = False
            
    return answer
