# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

def play(sr, sc, N):
    r, c = sr, sc
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1

    while True:
        cnt, (dr, dc) = board[r][c]

        for _ in range(cnt):
            r = (r + dr) % N
            c = (c + dc) % N

            if visited[r][c]:
                return sum(map(sum, visited))
            visited[r][c] = 1

def parse_cell(cell):
    return int(cell[:-1]), direction[cell[-1]]

# 입력
N = int(input())
gr, gc = map(lambda x: int(x)-1, input().split())
pr, pc = map(lambda x: int(x)-1, input().split())

# 방향 맵
direction = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

# 보드 파싱
board = [ [parse_cell(cell) for cell in input().split()] for _ in range(N) ]

# 게임 실행
g_score = play(gr, gc, N)
p_score = play(pr, pc, N)

# 출력
if g_score > p_score:
    print("goorm", g_score)
else:
    print("player", p_score)
