# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())

lst = []
for _ in range(n):
	s, p = input().split()
	p = int(p)
	lst.append([s, p])

lst.sort(key=lambda x: x[1])

print(*lst[-1])
print(*lst[0])
