# coding=utf-8
import random


class Guess(object):

    def __init__(self):
        self.answer = []
        self.c = []  # 创建一个空列表来放A和B
        self.k = 0

    def randomanswer(self):
        # 随机生成4位数0-9
        while len(self.answer) < 4:
            b = str(random.randint(0, 9))
        # 如果a列表有重复的数就不加入
            if b not in self.answer:
                self.answer.append(b)
        self.mystr = ''.join(self.answer)
        print self.mystr

    def playerInput(self):
        # self.k = 0
        while True:
            self.player = raw_input('请输入一个各个位数都不同的四位数，来猜这个数。')
            # player = str(player)
            # 判断输入的为数字

            if self.player.isdigit() and len(self.player) == 4:
                # 输入的数字不重复否则重新输入
                for i in range(4):
                    num = self.player.count(self.player[i])
                    # print num
                    if num > 1:
                        break
                # 查看没个数出现的次数，如果num为1，则执行ruler()

                if num == 1:

                    self.ruler()
                    # print num

    # 3.匹配这个数

    def ruler(self):
        self.c = []  # 每次清空列表C

        # 如果相同位置一样则输出一个A,否则看这个位置的数是否在另一个字符串里，在则输出一个B
        for i in range(4):
            if self.player[i] == self.mystr[i]:
                self.c.append('A')
            else:
                if self.player[i] in self.mystr:
                    self.c.append('B')
        self.c = sorted(self.c)
        self.myc = ''.join(self.c)
        print self.myc
        if self.myc == "AAAA":
            print "你猜对了。"
            exit()
        self.times()
        
    def times(self):
        self.k += 1
        print '猜了%s次'%self.k
        if self.k == 15:
            print "猜错15次，游戏结束。"
            exit()
        

p1 = Guess()
p1.randomanswer()
p1.playerInput()
