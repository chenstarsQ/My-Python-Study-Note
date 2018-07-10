# -*- coding:utf-8 -*-
from sys import exit


def start():
    print("这是一个自制的文字游戏，你想看看这个游戏的背景吗？")
    print("如果你想看的话，请输入Yes，不想看的话，请输入No。")
    choice = input(">>")
    if choice == "Yes":
        background()
    elif choice == "No":
        go_school()
    else:
        print("请按照指定的命令控制此游戏。")
# 上面是一个游戏的启动程序，相当于点击开始按钮。


def background():
    print("""时间：离高考还有一个月
	地点：胜阳高中
	
	有这样一所高中
	
	
	t
	e
	s
	t
	
	
	
	
	
	
	
	""")


def go_school():
    print("test")


start()
