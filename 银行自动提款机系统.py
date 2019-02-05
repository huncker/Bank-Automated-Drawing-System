#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 银行自动提款机系统.py
@Author: Hocker
@Date  : 2019/1/25 21:07
@Emial :hockel@foxmail.com 
'''

"""
人
类名：Person
属性： 姓名 身份证号 电话号 卡
行为： 开户 查询 取款 存储 转账 锁定 解锁 补卡 销户 退出

卡
类名：Card
属性：卡号 密码 余额 
行为：

提款机
类名：ATM
属性：用户字典
行为：开户 查询 取款 存储 转账 锁定 解锁 补卡 销户 


管理员界面
类名：Admin
属性：
行为：管理员界面 管理员登录 系统功能界面 

"""
from admin import Admin
from atm import ATM
import time
import os
import pickle
from card import Card
from user import User

def main():
    # 管理员对象
    admin = Admin()
    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1
    # 提款机对象
    filePath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filePath,"rb")
    allUsers = pickle.load(f)
    print("*******************")
    print(allUsers)
    atm = ATM(allUsers)



    while True:
        admin.printSysFunctionView()

        # 等待用户的操作
        option = input("请输入您的操作： ")
        if option == "1":
            #开户
            atm.createUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMony()
        elif option == "4":
            atm.saveMony()
        elif option == "5":
            atm.tranferMony()
        elif option == "6":
            atm.checkPasswd()
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            atm.newCard()
        elif option == "0":
            atm.killUser()
        elif option == "t":
            if not admin.adminOption():
                #将当前系统中的用户信息保存到文件中
                absPath = os.getcwd()
                f = open(filePath,"wb")
                pickle.dump(atm.allUsers,f)
                f.close()
                return -1
        time.sleep(2)

if __name__ == '__main__':
    main()
