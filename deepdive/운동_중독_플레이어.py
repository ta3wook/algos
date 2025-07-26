# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from math import floor

w, r = map(int, input().split())
res = floor((w * (1 + (r/30))))
print(res)
