import pickle

shoplistfile = 'D:\\pythontest\\shoplist.data'
# 指定文件，如没有则在该位置下创建
shoplist = ['apple','mango','carrot']


f = open(shoplistfile,'wb')
# 以二进制写入文件
pickle.dump(shoplist,f)
f.close()

del shoplist

f = open(shoplistfile,'rb')
# 以二进制阅读文件
storedlist = pickle.load(f)
# 载入文件
print(storedlist)

