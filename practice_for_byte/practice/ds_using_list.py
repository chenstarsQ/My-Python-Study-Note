#this is my shopping list
shoplist = ['apple','mango','carrot','banana']
print('T have',len(shoplist),'item to purchase')
print('Thesr items are :',end=' ')
#指定以空白结尾——不换行
for item in shoplist:
    print(item,end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now',shoplist)
print('I will sort my list now')
shoplist.sort()
print('Sorted shopping list is',shoplist)
print('The first item I will buy is ',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)
help(shoplist.sort())
