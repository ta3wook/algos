# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

t = int(input())

res = 0

for _ in range(t):
	a, op, b = input().split()
	a, b = map(int, [a, b])

	if op == '+':
		res += a + b
	elif op == '-':
		res += a - b
	elif op == '/':
		res += a // b
	elif op == '*':
		res += a * b

print(res)
