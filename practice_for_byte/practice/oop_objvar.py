class Robot:
    """表示一个带有名字的机器人。"""
    # 一个类变量，用来记数机器人的数量。
    population = 0 # 属Robot类 为类变量

    def __init__(self,name):  # name 变量属于对象（通过self分配）
        """初始化数据"""      # 为对象变量
        self.name = name
        print("(Initializing {})".format(self.name))

        # 当有人被创建时，机器人将会增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destoryed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robotw working.".format(
                Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候

        没问题，你做得到！"""
        print("Greatings,my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前的人口总量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C - 3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work.So let's destory them.")
droid1.die()
droid2.die()

Robot.how_many()
