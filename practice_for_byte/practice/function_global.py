x=50
def func():
    global x
    print('x is',x)
    x=2
    print('changed global x to',x)
func()
print('value of x is ',x)
##name 'x' is parameter and global
#变量不能同时作为global变量和函数之间传递的变量!!!
