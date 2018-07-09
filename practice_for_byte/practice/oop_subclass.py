class SchoolMember:
# 公共类 \Bass Class \Superclass
    '''代表任何学校里的成员。'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        '''告诉我有关我的细节。'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember):
# 子类1
    '''代表一位老师。'''
    def __init__(self,name,age,salary):
        #self.name = name
        #self.age = age
        SchoolMember.__init__(self,name,age)
        # 显式调用
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))

class Student(SchoolMember):
# 子类2
    '''代表一位学生。'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Students:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{:d}"'.format(self.marks))

t = Teacher('Mrs.Shrividya',40,30000)
s = Student('Swaroop',25,75)
# 实例
# 打印一行空白行
print()

members = [t, s]
for member in members:
    #对全体师生工作
    member.tell()
                                # t-->Teacher('Mrs.Shrividya',40,30000) --> class Teacher
# member --> members -->[t,s] -->                                                           -->print tell()
                                # s-->Student('Swaroop',25,75)          --> class Student
