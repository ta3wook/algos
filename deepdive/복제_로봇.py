# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

x, y = map(int, input().split())
n = int(input())

pond = []
for _ in range(n):
	pond.append(list(map(int, input().split())))
	
q = int(input())
cmd = list(input().split())

for c in cmd:
	tmpx, tmpy = x, y

	if c == 'L':
		tmpx -= 1
	elif c == 'R':
		tmpx += 1
	elif c == 'U':
		tmpy += 1
	elif c == 'D':
		tmpy -= 1

	if [tmpx, tmpy] not in pond:
		x, y = tmpx, tmpy

print(x, y)
