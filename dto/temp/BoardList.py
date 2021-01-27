from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from datasource import Base

__all__ = ['BoardList']

class BoardList(Base):
    __tablename__ = "board_list"
    __table_args__ = {
                        'comment' : '게시판 리스트'
    }

    BOARD_LIST_ID                        = Column(VARCHAR(100), primary_key=True, comment='게시판 리스트 id')
    BOARD_LIST_NAME                      = Column(VARCHAR(100), nullable=False, comment='게시판 이름')
    
    def __init__(self, blId, **kwargs):
        self.BOARD_LIST_ID = blId
        self.BOARD_LIST_NAME                       = kwargs.get('BOARD_LIST_NAME', None)

    def __repr__(self):
        return "{'BOARD_LIST_ID' : '%s', \
        'BOARD_LIST_NAME' : '%s'}" % (
                    self.BOARD_LIST_ID,
                    self.BOARD_LIST_NAME)