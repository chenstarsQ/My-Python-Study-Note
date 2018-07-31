#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-31 18:17:44
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$


def dayUP(df):
    dayup = 1
    for i in range(1, 366):
        if i % 7 in [6, 0]:
            dayup = dayup * (1-0.01)
        else:
            dayup = dayup * (1+df)
    return dayup


dayfactor = 0.01
while dayUP(dayfactor) < 37.78:
    dayfactor += 0.001
