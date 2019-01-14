#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-27 21:56:43
# @Author  : Star (1140330611@qq.com)
# @Link    : https://github.com/chenstarsQ/My-Python-Study-Note
# @Version : $Id$

from random import random


def printInto():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0-1之间的小数表示）")


def getInputs():
    a = eval(input("请输入选手A的能力值(0-1)："))
    b = eval(input("请输入选手B的能力值(0-1)："))
    n = eval(input("模拟N场比赛的场次："))
    return a, b, n


def gameover(a, b):
    return a == 15 or b == 15


def simOneGame(probA, probB):
    scoreA, scoreB = 0, 0
    serving = "A"
    while not gameover(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB


def simNGames(n, probA, probB):
    winsA, winsB = 0, 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB


def printSummary(winsA, winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛。占比{:0.1%}".format(winsA, winsA/n))
    print("选手B获胜{}场比赛。占比{:0.1%}".format(winsB, winsB/n))


def main():
    printInto()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


main()
