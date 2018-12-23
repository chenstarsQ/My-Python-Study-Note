#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-07 21:28:07
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

from random import random
from time import perf_counter
DARTS = 10000*10000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x**2 + y**2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4*(hits/DARTS)
print("圆周率是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter()-start))
