#类定义

#括号中的Object表示该类继承于Object
class Person(object):
    def __init__(self,name,score):
        # __name 为私有变量，private
        # score 为公共变量，可被外部访问，public
        self.__name = name
        self.score = score
        self.initImpression()

    def getName(self):
        return self.__name

    def initImpression(self):
        if self.score < 20:
            self.impression = 0
        elif self.score < 40:
            self.impression = 20
        elif self.score < 60:
            self.impression = 40
        else:
            self.impression = 41

    def printScore(self):
        print('%s score is %s' % (self.__name,self.score))

    def addImpression(self, impression):
        self.impression += impression

    def getImpression(self):
        if self.impression < 0:
            self.attitude = '陌路'
        elif self.impression < 20:
            self.attitude = '融洽'
        elif self.impression < 40:
            self.attitude = '结为好友'
        elif self.impression < 60:
            self.attitude = '邀为同道'
        elif self.impression < 80:
            self.attitude = '两情相悦'
        else:
            self.attitude = '喜结连理'
        return  self.attitude


stu = Person('Lilith',80)
print(stu.getName())
# 私有变量调用为 __name自动编译为 _(类名)__name
# 不同版本解释器可能存在不同的自动编译命名
print(stu._Person__name)
print(stu.score)
stu.printScore()
print(stu.getImpression())

def Student(Person):
    pass