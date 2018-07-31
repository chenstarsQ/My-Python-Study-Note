#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-13 20:33:13
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

# PythonDraw.py
import turtle  # 导入绘图库turtle
turtle.setup(650, 350, 200, 200)  # 设置窗口位置
turtle.penup()  # 提笔
turtle.fd(-250)  # 朝turtle头部前进(forward)-250像素，即后退250像素
turtle.pendown()  # 落笔
turtle.pensize(50)  # 设置笔尖大小为50像素的圆
turtle.pencolor("purple")  # 设置笔的颜色为紫色
turtle.seth(-40)  # 设定绝对角度
for i in range(4):  # 循环绘制圆弧
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(50, 180)
turtle.fd(40*2/3)
turtle.done()  # 表示暂停绘制，绘图窗口不关闭
