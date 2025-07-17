def solution(N, stages):
    answer = []
    
    status = [[0, 0] for _ in range(N)]
    for stage in stages:
        if stage > 1:
            for i in range(min(stage, N)):
                status[i][0] += 1
            if stage <= N:
                status[stage-1][1] += 1
        else:
            status[0][0] += 1
            status[0][1] += 1
    
    failrate = [[i, 0] for i in range(1, N+1)]
    for i, stat in enumerate(status):
        if stat[0] != 0:
            failrate[i][1] = stat[1] / stat[0]
        else:
            failrate[i][1] = 0

    failrate.sort(key=lambda x : x[1], reverse=True)
    
    for fail in failrate:
        answer.append(fail[0])
    
    return answer
