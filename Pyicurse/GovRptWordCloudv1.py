#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-23 18:28:14
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

import jieba
import wordcloud
from scipy.misc import imread
mask = imread("fivestar.jpg")
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000,
                        height=700, background_color="white", mask=mask,)
w.generate(txt)
w.to_file("grwordcloud.png")
