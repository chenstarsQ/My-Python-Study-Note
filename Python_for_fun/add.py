#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-14 19:50:37
# @Author  : Star (1140330611@qq.com)
# @Link    : ${link}
# @Version : $Id$

A = 0
B = 0
i = 0
add = 1
while add:
    i = i+1
    A += 1
    B += A
    if i == 100:
        break
print(B)
