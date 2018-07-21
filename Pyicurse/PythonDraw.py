#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-13 20:33:13
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

# PythonDraw.py
import turtle  # 导入绘图库turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(50)
turtle.pencolor("red")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(50, 180)
turtle.fd(40*2/3)
turtle.done()
