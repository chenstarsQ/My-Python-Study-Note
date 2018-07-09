import os
import time
# 1. 需要备份的文件与目录将被
# 指定在一个列表中。
# 例如在 Windows 下：
source = ['D:\\pythontest\\backup" "test\\*']#windows cmd 无法识别空格
# 在这里要注意到我们必须在字符串中使用双引号
# 用以括起其中包含空格的名称。

#2. 备份文件必须存储在一个
#主备份目录中
#例如在 Windows 下：
target_dir = r'D:\pythontest\backup'
# 3. 备份文件将打包压缩成 zip 文件。
# 4. zip 压缩文件的文件名由当前日期与时间构成。
target = target_dir + os.sep + \                 #os.sep : 分隔符
         time.strftime('%Y%m%d%H%M%S') + '.zip'
# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    print('we don\'t have this file' )
    os.mkdir(target_dir)
else:
    print('we already have this file')
# 创建目录\\仅可以创建末尾文件夹
# 5. 我们使用 haozip 命令将文件打包成 zip 格式
HaoZipC_command ='HaoZipC a -tzip {0} {1} -w{2}'.format(target,
                                            ' '.join(source),target_dir)
# ' '.join():''分隔符，''可空
# 运行备份
print('Zip command is:')
print(HaoZipC_command)
print('Running:')
if os.system(HaoZipC_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
