# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

t = int(input())

res = 0
for i in range(t):
	tmp1, tmp2 = map(int, input().split())
	
	a = min(tmp1, tmp2)
	b = max(tmp1, tmp2)

	if b*100 >= a*160 and b*100 <= a*163:
		res += 1

print(res)
