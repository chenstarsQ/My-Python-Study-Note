#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 21:52:16
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
f.close()

for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
