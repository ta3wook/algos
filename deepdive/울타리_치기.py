# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
a = list(map(int, input().split()))

res = 2 * n

if n == 1:
	res += 2 * a[0]
else:
	for i in range(n):
		if i == 0:
			res += a[i] + max(a[i] - a[i+1], 0)
		elif i == n-1:
			res += a[i] + max(a[i] - a[i-1], 0)
		else:
			res += max(a[i] - a[i+1], 0) + max(a[i] - a[i-1], 0)

print(res)
