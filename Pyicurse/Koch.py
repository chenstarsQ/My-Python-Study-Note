#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-20 21:44:14
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)


def main():
    print("请输入需要绘制的科赫雪花阶数（≥0的整数）")
    level = eval(input())
    turtle.setup(600, 600)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.right(120)
    koch(400, level)
    turtle.hideturtle()
    turtle.done()

main()
