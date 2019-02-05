#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : atm.py
@Author: Hocker
@Date  : 2019/2/5 14:09
@Emial :hockel@foxmail.com 
'''
from card import Card
from user import User
import random
import time
class ATM(object):
    def __init__(self,allUser):
        self.allUsers = allUser#卡号-用户
    #开户
    def createUser(self):
        #目标：向用户字典中添加一对键值对（卡号-用户）
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone = input("请输入您的电话号码：")

        prestoreMoney = int(input("请输入您的预存款："))
        if prestoreMoney < 0 :
            print("预存款输入有误！！开户失败")
            return -1
        onePasswd = input("请设置密码：")
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误！！开户失败...")
            return -1

        #所有需要的信息就全了
        cardStr = self.randomCardId()

        card = Card(cardStr,onePasswd,prestoreMoney)
        user = User(name,idCard,phone,card)
       #存到字典
        self.allUsers[cardStr] = user
        print("开户成功，请牢记卡号(%s)...." % (cardStr))

    #查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        #验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        print("账号：%s  余额：%d" % (user.card.cardId,user.card.cardMoney))
    #取款
    def getMony(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        # 取款
        money = int(input("请输入取款金额："))
        if money > user.card.cardMoney:
            print("余额不足，取款失败！")
            return -1
        if money <= 0:
            print("输入错误，取款失败！")
            return -1
        user.card.cardMoney -= money
        print("取款成功！余额=%d" %(user.card.cardMoney))

    #存储
    def saveMony(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        # 取款
        money = int(input("请输入存款金额："))
        if money < 0:
            print("请输入正确存款金额！")
            return -1
        if money > user.card.cardMoney:
            print("余额不足，取款失败！")
            return -1
        user.card.cardMoney += money
        print("存款成功！余额=%d" % (user.card.cardMoney))
    #
    def tranferMony(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        # 转账
        tranferUserNum = input("请输入你要转账的卡号：")
        money = int(input("请输入转账金额："))
        if not self.allUsers.get(tranferUserNum) :
            print("请输入正确转账卡号：")
            return -1
        user.card.cardMoney -= money
        # 到账账户的金钱变动
        tranferUser = self.allUsers.get(tranferUserNum)
        tranferUser.card.cardMoney += money
        print("转账成功，您的账户余额：%d" % (user.card.cardMoney))

    def changePasswd(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        #改密
        newPasswd = input("请你输入新的密码：")
        user.card.cardPasswd = newPasswd
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        #锁它
        user.card.cardLock = True
        print("锁定成功")
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1

        # 解锁
        user.card.cardLock = False
        print("解锁成功")

    def newCard(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1
        newCard = self.randomCardId()
        self.allUsers.pop(cardNum)
        self.allUsers[newCard] = user
        print("您的新卡号为：%s\n已为您将余额转存入该卡，请妥善保管！" % (newCard))
        print("(系统将在 5 秒后自动返回……)")


    def killUser(self):
        cardNum = input("请输入您要销户的卡号：")
        # 验证是否存在该卡号
        user = self.allUsers.get(cardNum)
        if self.checkFunc(cardNum, user):
            return 1

        print("操作成功！请稍候……")
        self.allUsers.pop(cardNum)
        time.sleep(2)
        print("该卡号已注销……\n(系统将在 5 秒后自动返回……)")
        time.sleep(5)

#验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd :
                return True

        return False

#生成卡号
    def randomCardId(self):

        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str += ch
            #判断是否重复
            if not self.allUsers.get(str):
                return str
# 检查函数
    def checkFunc(self, cardNum, user):
        if cardNum == "t":
            return 1
        if not user:
            print("该卡号不存在!!操作失败……")
            return 1
        #判断是否锁定
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后重试……")
            return 1
        #验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！该卡已被锁定！！请解锁后重试……")
            user.card.cardLock = True
            return
