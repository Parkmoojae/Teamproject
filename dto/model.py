# coding: utf-8
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

# pip install sqlacodegen
Base = declarative_base()
metadata = Base.metadata


class Auth(Base):
    __tablename__ = 'auth'
    __table_args__ = {'comment': '권한'}

    auth_id = Column(String(100), primary_key=True, comment='게시판 권한 id')
    user_group_id = Column(String(100), comment='회원그룹 id')
    board_id = Column(INTEGER(11), comment='게시판 id')
    auth_board_write = Column(TINYINT(4), comment='작성 권한 / 가능:1 없음:0')
    auth_board_del = Column(TINYINT(4), comment='삭제 권한 / 가능:1 없음:0')
    auth_board_modi = Column(TINYINT(4), comment='수정 권한 / 가능:1 없음:0')
    auth_board_read = Column(TINYINT(4), comment='조회 권한 / 가능:1 없음:0')
    auth_comment_del = Column(TINYINT(4), comment='댓글 삭제 권한 / 가능:1 없음:0')
    auth_comment_write = Column(TINYINT(4), comment='댓글 작성 권한 / 가능:1 없음:0')


class Board(Base):
    __tablename__ = 'board'
    __table_args__ = {'comment': '게시판 공통'}

    board_id = Column(INTEGER(11), primary_key=True, comment='게시글 아이디')
    board_content = Column(String(255), comment='게시글 내용')
    user_id = Column(String(100), comment='회원 id')
    board_regdate = Column(DateTime, comment='게시글 등록일')
    board_del = Column(TINYINT(4), comment='게시글 삭제여부/일반:0 삭제:1')
    board_list_id = Column(String(100), comment='게시판 리스트 아이디')
    board_title = Column(String(100), comment='게시글 제목')
    board_pid = Column(INTEGER(11), comment='게시글 pid')


class BoardList(Base):
    __tablename__ = 'board_list'
    __table_args__ = {'comment': '게시판 리스트'}

    board_list_id = Column(String(100), primary_key=True, comment='게시판 리스트 id')
    board_list_name = Column(String(100), comment='게시판 이름')


class Comment(Base):
    __tablename__ = 'comment'
    __table_args__ = {'comment': '댓글'}

    comment_id = Column(INTEGER(11), primary_key=True, comment='댓글 id')
    comment_pid = Column(INTEGER(11), comment='댓글 pid')
    board_id = Column(INTEGER(11), comment='게시글 id')
    comment_content = Column(String(100), comment='댓글 내용')
    comment_del = Column(TINYINT(4), comment='댓글 삭제여부 / 일반:0 삭제:1')
    user_id = Column(String(100), comment='회원 id')
    comment_regdate = Column(DateTime, comment='댓글 등록일')
    board_list_id = Column(String(100), comment='게시판 id')


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'comment': '회원 정보'}

    user_id = Column(String(100), primary_key=True, comment='회원 아이디')
    user_pw = Column(String(100), comment='회원 비밀번호')
    user_group_id = Column(String(100), comment='회원 그룹아이디')


class UserGroup(Base):
    __tablename__ = 'user_group'
    __table_args__ = {'comment': '회원 등급'}

    user_group_id = Column(String(100), primary_key=True, comment='회원등급 id')
    user_group_name = Column(String(100), comment='회원등급 이름')