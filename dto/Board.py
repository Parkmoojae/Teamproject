from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from dataSource import Base

__all__ = ['Board']

class Board(Base):
    __tablename__ = "Board"
    __table_args__ = {
                        'comment' : '게시판 공통'
    }

    BOARD_ID                             = Column(Integer, primary_key=True, autoincrement=True, comment='게시글 id')
    BOARD_CONTENT                        = Column(VARCHAR(255), nullable=False, comment='게시글 내용')
    USER_ID                              = Column(VARCHAR(100), nullable=False, comment='회원 id')
    BOARD_REGDATE                        = Column(DATETIME, comment='게시글 등록일')
    BOARD_DEL                            = Column(BOOLEAN, comment='게시글 삭제여부 / 일반:0 삭제:1')
    BOARD_LIST_ID                        = Column(VARCHAR(100), comment='게시판 리스트 id')
    BOARD_TITLE                          = Column(VARCHAR(100), comment='게시글 제목')
    BOARD_PID                            = Column(Integer, comment='게시글 pid')
    
    def __init__(self, **kwargs):
        self.BOARD_ID                            = kwargs.get('BOARD_ID', None)
        self.BOARD_CONTENT                       = kwargs.get('BOARD_CONTENT', None)
        self.USER_ID                             = kwargs.get('USER_ID', None)
        self.BOARD_REGDATE                       = kwargs.get('BOARD_REGDATE', None)
        self.BOARD_DEL                           = kwargs.get('BOARD_DEL', None)
        self.BOARD_LIST_ID                       = kwargs.get('BOARD_LIST_ID', None)
        self.BOARD_TITLE                         = kwargs.get('BOARD_TITLE', None)
        self.BOARD_PID                           = kwargs.get('BOARD_PID', None)

    def __repr__(self):
        return "{'BOARD_ID' : '%s', \
        'BOARD_CONTENT' : '%s', \
        'USER_ID' : '%s', \
        'BOARD_REGDATE' : '%s', \
        'BOARD_DEL' : '%s', \
        'BOARD_LIST_ID' : '%s', \
        'BOARD_TITLE' : '%s', \
        'BOARD_PID' : '%s'}" % (
                    self.BOARD_ID,
                    self.BOARD_CONTENT,
                    self.USER_ID,
                    self.BOARD_REGDATE,
                    self.BOARD_DEL,
                    self.BOARD_LIST_ID,
                    self.BOARD_TITLE,
                    self.BOARD_TITLE)