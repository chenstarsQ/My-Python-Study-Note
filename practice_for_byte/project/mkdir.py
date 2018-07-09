import os

a=r'D:\tttt'
if not os.path.exists(a):
    print('not have a')
    os.mkdir(a)
print('done')
