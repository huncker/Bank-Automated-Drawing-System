#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : card.py
@Author: Hocker
@Date  : 2019/2/5 17:06
@Emial :hockel@foxmail.com 
'''
class Card(object):
    def __init__(self,cardId,cardPasswd,cardMoney):
        self.cardId = cardId
        self.cardPasswd = cardPasswd
        self.cardMoney = cardMoney
        self.cardLock = False