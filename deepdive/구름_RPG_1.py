# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())

res = []
for _ in range(n):
	a = int(input())
	tmp = 'Yes'

	if a > 2:
		for i in range(2, int(a ** 0.5) + 1):
			if a % i == 0:
				tmp = 'No'
				break
				
	res.append(tmp)

for r in res:
	print(r)
