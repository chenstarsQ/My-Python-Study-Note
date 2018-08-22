#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-10 21:06:48
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

import time
for i in range(101):
    print("\r{:3}%".format(i), end=" ")
    time.sleep(0.1)
