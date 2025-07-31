# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())

alice = list(map(int, input().split()))
bob = list(map(int, input().split()))

res = [0, 0]
for a, b in zip(alice, bob):
	if abs(a - b) == 7:
		if a < b:
			res[0] += 3
			res[1] -= 1
		else:
			res[0] -= 1
			res[1] += 3
	elif a > b:
		res[0] += 2
	elif a < b:
		res[1] += 2
	else:
		res[0] += 1
		res[1] += 1

print(*res)
