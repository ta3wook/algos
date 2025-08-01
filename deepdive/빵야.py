# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
h = list(map(int, input().split()))

res = 0
bullet = 0

dmg = [1, 2, 3, 4]
dmgCyc = 10

for hp in h:
	for i in range(bullet, len(dmg)):
		hp -= dmg[i]
		res += 1
		bullet += 1
		if hp <= 0:
			break
	bullet %= 4
	if hp <= 0:
		continue
		
	res += (hp // dmgCyc) * 4
	
	hp = hp % dmgCyc
	for d in dmg:
		if hp <= 0:
			break
		hp -= d
		res += 1
		bullet += 1

print(res)
