import pymysql
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import create_engine, Table, Column, Integer, Date, String, MetaData, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import DateTime

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer())
    birthday = Column(Date())
    sex = Column(String(1))
    education = Column(String(50))
    create_time = Column(DateTime(), server_default=func.now())
    update_time = Column(DateTime(), server_default=func.now(),
                         server_onupdate=func.now())


db_url = "mysql+pymysql://root:xxx@xxx:3306/testdb?charset=utf8mb4"
engine = create_engine(db_url, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)

db = pymysql.connect(host='xxx', user='root', password="xxx", database='testdb', port=3306,
                     charset='utf8mb4')

try:
    with db.cursor() as cursor:
        sql = 'insert into user (name,age,birthday,sex,education) values (%s,%s,%s,%s,%s)'
        values = (
            ("李七", 23, "1997-01-01", '1', 'Bachelor'),
            ("张八", 24, "1996-02-02", '0', 'Master'),
            ("赵九", 25, "1995-03-03", '1', 'Doctor'),
        )
        cursor.executemany(sql, values)
        # 查
        sql = 'select * from user'
        cursor.execute(sql)
        users = cursor.fetchall()
        for user in users:
            print(user)
    db.commit()
except Exception as e:
    print(f"insert error {e}")
finally:
    db.close()
