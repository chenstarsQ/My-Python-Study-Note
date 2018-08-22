#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 17:04:17
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$


class Room(object):
    def __init__(self, name, description):  # 定义__init__方法，初始化Room类
        self.name = name  # name返回name
        self.description = description  # description返回description
        self.paths = {}  # paths返回空{}（字典）
        # 即类中的name、description都为字典类型，默认为空字典

    def go(self, direction):  # 定义go方法，go 位置、方向
        return self.paths.get(direction, None)  # get方法，从键值获取字典direction值

    def add_paths(self, paths):  # 定义add方法，添加字典值
        self.paths.update(paths)  # update方法，给字典中增加键值
