from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    ind = deque(range(len(q)))
    
    res = []
    while q:
        tmp = q.popleft()
        tmpInd = ind.popleft()

        if max(q, default=0) > tmp:
            q.append(tmp)
            ind.append(tmpInd)
        else:
            res.append(tmpInd)
            if tmpInd == location:
                break
    
    answer = len(res)
    return answer
