from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    answer = 'Yes'
    while goal:
        tmp = goal.popleft()
        if cards1 and tmp == cards1[0]:
            cards1.popleft()
        elif cards2 and tmp == cards2[0]:
            cards2.popleft()
        else:
            answer = 'No'
            break
    
    return answer
