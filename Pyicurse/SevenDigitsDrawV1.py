#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-11 14:41:40
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

import turtle
import time


def drawGarp():
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):
    drawGarp()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGarp()
    turtle.right(90)


def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4,
                                5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == "/":
            turtle.write("年", font=("Arial", 18,  "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "*":
            turtle.write("月", font=("Arial", 18,  "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "-":
                turtle.write("日", font=("Arial", 18, "normal"))
                turtle.fd(40)
        else:
            drawDigit(eval(i))


def main():
    print("请输入时间，如'2018/10*20-',若要绘制系统当前时间，请输入'time'")
    date = input()
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    if date == "time":
        drawDate(time.strftime("%Y/%m*%d-", time.gmtime()))
    else:
        drawDate(date)
    turtle.penup()
    turtle.done()

main()
