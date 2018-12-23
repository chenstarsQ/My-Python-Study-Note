#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-31 22:06:08
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

height, weight = eval(input("请输入身高和体重，以逗号隔开"))
bmi = weight / pow(height, 2)
print("BMI 数值为:{:.2f}".format(bmi))

