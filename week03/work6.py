'''
CREATE TABLE `user2` (
  `id` char(4) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `user2` VALUES ('1001', '张三');
INSERT INTO `user2` VALUES ('1002', '李四');


CREATE TABLE `Account` (
  `id` char(4) NOT NULL,
  `money` double(9,3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `zichan` VALUES ('1001', '1100.120');
INSERT INTO `zichan` VALUES ('1002', '604.060');


CREATE TABLE `audit` (
  `time` datetime DEFAULT NULL,
  `from_id` char(4) DEFAULT NULL,
  `to_id` char(4) DEFAULT NULL,
  `money` double(9,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;'''

import uuid

import pymysql
from datetime import datetime


class TransferMoney(object):

    def __init__(self, db):
        self.db = db

    def check_id(self, id):
        cursor = self.db.cursor()
        try:
            sql = "select * from user2 where id = '%s'" % id
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) < 1:
                raise Exception("账号%s不存在" % id)
        finally:
            cursor.close()

    def check_balance(self, id, money):
        cursor = self.db.cursor()
        try:
            sql = "select money from Account where id=%s and money>%s" % (
                id, money)
            cursor.execute(sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("余额不足")
        finally:
            cursor.close()

    def transfer_money(self, id, money):
        cursor = self.db.cursor()
        try:
            sql = "update Account set money = money+%s where id = '%s'" % (
                    money, id)
            cursor.execute(sql)
            if cursor.rowcount != 1:
                raise Exception("转账失败")
        finally:
            cursor.close()

    # 转账
    def transfer(self, from_id, to_id, money):
        try:
            self.check_id(from_id)
            self.check_id(to_id)
            self.check_balance(from_id, money)
            self.transfer_money(from_id, -money)
            self.transfer_money(to_id, money)
        except Exception as e:
            self.db.rollback()
            raise e


if __name__ == '__main__':
    to_id = '1002'
    from_id = '1001'
    money = 100
    db = pymysql.connect("xxx", "root", "xxx", "testdb")
    TransferSystem = TransferMoney(db)
    try:
        TransferSystem.transfer(from_id, to_id, money)
        atime = datetime.now()
        aid = str(uuid.uuid4())
        sql = "INSERT INTO audit (id,time,from_id,to_id,money) Values(%s,%s,%s,%s,%s)"
        value = (aid, atime, from_id, to_id, money)
        db.cursor().execute(sql, value)
        db.commit()
    except Exception as e:
        print(f'转账出问题了: {e}')
    finally:
        db.close()