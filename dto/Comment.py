from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, BOOLEAN, NUMERIC
from datasource import Base

__all__ = ['Comment']

class Comment(Base):
    __tablename__ = "comment"
    __table_args__ = {
                        'comment' : '게시판 댓글'
    }

    COMMENT_ID                           = Column(Integer, primary_key=True, comment='댓글 id')
    COMMENT_PID                          = Column(Integer, nullable=False, comment='댓글 pid')
    BOARD_ID                             = Column(Integer, nullable=False, comment='게시글 id')
    COMMENT_CONTENT                      = Column(VARCHAR(100), comment='댓글 내용')
    COMMENT_DEL                          = Column(BOOLEAN, comment='댓글 삭제여부 / 일반:0, 삭제:1')
    USER_ID                              = Column(VARCHAR(100), comment='회원 ID')
    COMMENT_REGDATE                      = Column(DATETIME, comment='댓글 등록일')
    
    def __init__(self, commentId, **kwargs):
        self.COMMENT_ID = commentId
        self.COMMENT_PID                         = kwargs.get('COMMENT_PID', None)
        self.BOARD_ID                            = kwargs.get('BOARD_ID', None)
        self.COMMENT_CONTENT                     = kwargs.get('COMMENT_CONTENT', None)
        self.COMMENT_DEL                         = kwargs.get('COMMENT_DEL', None)
        self.USER_ID                             = kwargs.get('USER_ID', None)
        self.COMMENT_REGDATE                     = kwargs.get('COMMENT_REGDATE', None)

    def __repr__(self):
        return "{'COMMENT_ID' : '%s', \
        'COMMENT_PID' : '%s', \
        'BOARD_ID' : '%s', \
        'COMMENT_CONTENT' : '%s', \
        'COMMENT_DEL' : '%s', \
        'USER_ID' : '%s', \
        'COMMENT_REGDATE' : '%s'}" % (
                    self.COMMENT_ID,
                    self.COMMENT_PID,
                    self.BOARD_ID,
                    self.COMMENT_CONTENT,
                    self.COMMENT_DEL,
                    self.USER_ID,
                    self.COMMENT_REGDATE,)