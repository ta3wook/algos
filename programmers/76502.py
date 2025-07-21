def solution(s):
    answer = 0
    open = ['(','{', '[']
    close = [')','}', ']']
    
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            tmp = s[(j+i)%len(s)]
            if tmp in open:
                stack.append(tmp)
            elif tmp in close:
                if stack:
                    lst = stack[-1]
                    if tmp == ')' and lst == '(':
                        stack.pop()
                    elif tmp == ']' and lst == '[':
                        stack.pop()
                    elif tmp == '}' and lst == '{':
                        stack.pop()
                    else:
                        stack.append(tmp)
                else:
                    stack.append(tmp)
                    
        if not stack: # empty
            answer += 1
        
    return answer
