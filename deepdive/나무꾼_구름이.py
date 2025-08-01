# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, m, x = map(int, input().split())
h = list(map(int, input().split()))
q = int(input())
dir = list(input().split())

x -= 1
res = 0
for eps, d in enumerate(dir):
	if h[x] + eps >= m:
		res += h[x] + eps
		h[x] = -eps
	if d == 'L':
		x = (x - 1) if x > 0 else n - 1
	elif d == 'R':
		x = (x + 1) if x < n - 1 else 0
	elif d == 'S':
		pass

print(res)
