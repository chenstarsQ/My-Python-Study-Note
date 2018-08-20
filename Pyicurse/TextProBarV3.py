#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 21:19:53
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

import time
scale = 100
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = "*"*i
    b = '.'*(scale-i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2, "-"))
