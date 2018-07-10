def total(a=5,*numbers,**phonebook):
    print('a',a)

    #遍历元组中所有的项目
    for single_item in numbers:
        print('singel_item',single_item)
    #遍历字典中所有项目
    for first_part,second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,3,12,444,jack=321,jhon=532,inge=432423))
