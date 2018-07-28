#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 16:50:43
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

from nose.tools import *
from ex47.game import Room


def setup():
    print("SETUP")


def teardown():
    print("TEAR DOWN")


def test_basic():
    print("I RAN")
