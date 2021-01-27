from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from datasource import Base

__all__ = ['User']

class User(Base):
    __tablename__ = "user"
    __table_args__ = {
                        'comment' : '회원 정보'
    }

    USER_ID                        = Column(VARCHAR(100), primary_key=True, comment='회원 아이디')
    USER_PW                        = Column(VARCHAR(100), nullable=False, comment='회원 비밀번호')
    
    def __init__(self, userId, **kwargs):
        self.USER_ID = userId
        self.USER_PW                       = kwargs.get('USER_PW', None)

    def __repr__(self):
        return "{'USER_ID' : '%s', \
        'USER_PW' : '%s'}" % (
                    self.USER_ID,
                    self.USER_PW)