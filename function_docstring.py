def print_max(x, y):
    ''' 打印两个数值中的最大数。

    这两个数都应该是整数'''

    #if will make it to zhengshu
    x = int(x)
    y = int(y)

    if x > y:
        print(x,'is maximum')
    else :
        print(y,'is maximum')
print_max(9, 8)
print(print_max.__doc__)


