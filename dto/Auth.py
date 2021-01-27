from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from dataSource import Base

__all__ = ['Auth']

class Auth(Base):
    __tablename__ = "auth"
    __table_args__ = {
                        'comment' : '게시판 권한'
    }

    AUTH_ID                              = Column(VARCHAR(100), primary_key=True, comment='게시판 권한 id')
    USER_GROUP_ID                        = Column(VARCHAR(100), nullable=False, comment='회원그룹 id')
    BOARD_ID                             = Column(Integer, nullable=False, comment='게시판 id')
    AUTH_BOARD_READ                      = Column(BOOLEAN, comment='게시판 조회 권한')
    AUTH_BOARD_WRITE                     = Column(BOOLEAN, comment='게시판 작성 권한')
    AUTH_BOARD_MODI                      = Column(BOOLEAN, comment='게시판 수정 권한')
    AUTH_BOARD_DEL                       = Column(BOOLEAN, comment='게시판 삭제 권한')
    AUTH_COMMENT_DEL                     = Column(BOOLEAN, comment='게시판 댓글 삭제 권한')
    AUTH_COMMENT_WRITE                   = Column(BOOLEAN, comment='게시판 댓글 작성 권한')
    
    def __init__(self, authId, **kwargs):
        self.AUTH_ID = authId
        self.USER_GROUP_ID                       = kwargs.get('USER_GROUP_ID', None)
        self.BOARD_ID                            = kwargs.get('BOARD_ID', None)
        self.AUTH_BOARD_READ                     = kwargs.get('AUTH_BOARD_READ', None)
        self.AUTH_BOARD_WRITE                    = kwargs.get('AUTH_BOARD_WRITE', None)
        self.AUTH_BOARD_MODI                     = kwargs.get('AUTH_BOARD_MODI', None)
        self.AUTH_BOARD_DEL                      = kwargs.get('AUTH_BOARD_DEL', None)
        self.AUTH_COMMENT_DEL                    = kwargs.get('AUTH_COMMENT_DEL', None)
        self.AUTH_COMMENT_WRITE                  = kwargs.get('AUTH_COMMENT_WRITE', None)

    def __repr__(self):
        return "{'AUTH_ID' : '%s', \
        'USER_GROUP_ID' : '%s', \
        'BOARD_ID' : '%s', \
        'AUTH_BOARD_READ' : '%s', \
        'AUTH_BOARD_WRITE' : '%s', \
        'AUTH_BOARD_MODI' : '%s', \
        'AUTH_BOARD_DEL' : '%s', \
        'AUTH_COMMENT_DEL' : '%s', \
        'AUTH_COMMENT_WRITE' : '%s'}" % (
                    self.AUTH_ID,
                    self.USER_GROUP_ID,
                    self.BOARD_ID,
                    self.AUTH_BOARD_READ,
                    self.AUTH_BOARD_WRITE,
                    self.AUTH_BOARD_MODI,
                    self.AUTH_BOARD_DEL,
                    self.AUTH_COMMENT_DEL,
                    self.AUTH_COMMENT_WRITE)