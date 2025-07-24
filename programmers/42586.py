from collections import deque

def solution(progresses, speeds):
    q = deque()
    
    for progress, speed in zip(progresses, speeds):
        dep = (100 - progress) // speed + (1 if (100 - progress) % speed != 0 else 0)
        q.append(dep)
    
    answer = []
    mx = 0
    while q:
        if answer:
            tmp = q.popleft()
            if mx >= tmp:
                answer[-1] += 1
            else:
                mx = tmp
                answer.append(1)
        else:
            mx = q.popleft()
            answer.append(1)
    
    return answer
