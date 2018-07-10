age = 20#定义age为数字（整数instegers）
name = 'Swaroop'#定义name为字符串

print('{0} was {1} years old when he wrote this book'.format(name,age))
#将name，age，替换至字符串
print('why is {0} playing with that python?'.format(name))
#将name替换至字符串

#print中的{0}、{1}表示相对应的部分，其中，0、1可不写


#format的作用：将定义的部分替换至字符串（{}）内。

print('{:33.3f}'.format(1.0/3))
#{}表示一种格式

# 0、1、.. .表示format中元素的序号（从0开始）（若仅有1元素，默认为0，可空下）

#：定义字符宽度，:10表示替换后元素前空10宽度，:^10表示替换后元素宽度为10

#.3f表示替换后元素保留三位小数

print('{0:_^11}'.format('hello'))
print('{name} wrote {book}'.format(name='Swaroop',book='A Byte Of Python'))
