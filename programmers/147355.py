def solution(t, p):
    
    totalLength = len(t)
    portionNumbers = []
    portionLength = len(p)
    
    answer = 0
    
    for i in range(totalLength - portionLength + 1):
        tmp = t[i:i+portionLength]
        portionNumbers.append(int(tmp))
    
    p = int(p)
    for number in portionNumbers:
        if number <= p:
            answer += 1
    
    return answer
