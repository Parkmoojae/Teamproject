from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from datasource import Base

__all__ = ['Usergroup']


class Usergroup(Base):
    __tableName__ = "user_group"
    __table_args__= {
                'comment' : '회원등급'
    }

    USER_GROUP_ID                   = Column(VARCHAR(100),primary_key = True, comment="회원등급 id")
    USER_GROUP_NAME                 = Column(VARCHAR(100), comment="회원등급 이름")
    

    def __init__(self, ugid, **kwargs):
        self.USER_GROUP_ID = ugid
        self.USER_GROUP_NAME                = kwargs.get('USER_GROUP_ID',None)

    def __def__(self):
        return "{ 'USER_GROUP_ID' : '%s',\
            'USER_GROUP_NAME' : '%s'}" %{
                self.USER_GROUP_ID,
                self.USER_GROUP_NAME
            }