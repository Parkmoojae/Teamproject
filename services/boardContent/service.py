from datasource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime, Integer, Sequence, literal, VARCHAR
from sqlalchemy.sql import bindparam
import uuid, datetime
from dto.model import Board, Comment
from ainUtil import *
from util import *


# 게시글 data 가져오기(DB)
def getBoardContent(data):
    print(data)
    queryResult = session.query(Board).\
                    with_entities(
                        Board.board_id, Board.board_content, Board.user_id, Board.board_regdate, Board.board_del,
                        Board.board_list_id, Board.board_title, Board.board_pid
                    ).\
                    filter(and_(Board.board_id==data['boardId']), (Board.board_list_id==data['boardListId']))
                    # filter(model.Board.board_list_id==data['boardListId'])
    
    print(queryResult.all())
    resultVal = queryToDict(queryResult)
    print("@@@@@@@getBoard@@@@@@@@@")
    print(resultVal)
    print(type(resultVal))

    return resultVal

# 댓글 DB삽입
def insertComment(data):
    comment = Comment(comment_pid = data['commentPid'],
                    board_id = data['boardId'],
                    comment_content = data['commentContent'],
                    comment_del = 0,
                    user_id = data['userId'],
                    comment_regdate = datetime.datetime.now(),
                    board_list_id = data['boardListId'])
    result = sessionAdd(comment, session)
    return result


# 댓글 리스트 가져오기(DB)
def getComment(data):
    treeQuery = session.query(Comment).\
                    with_entities(Comment.board_id, Comment.board_list_id, Comment.comment_content,
                                  Comment.comment_del, Comment.comment_id, Comment.comment_pid,
                                  Comment.comment_regdate, Comment.user_id,
                                  literal(0).label('depth'),
                                  (Comment.comment_id.cast(VARCHAR(10000))).label('lvl'),
                                  (func.lpad(Comment.comment_id, 10, '0').cast(VARCHAR(10000))).label('lvl2')
                                  ).\
                    filter(Comment.board_id==data['boardId'], Comment.board_list_id==data['boardListId'], Comment.comment_pid==0).\
                    cte('cte', recursive=True)

    uniTreeQuery = session.query(Comment).\
                        with_entities(Comment.board_id, Comment.board_list_id, Comment.comment_content,
                                      Comment.comment_del, Comment.comment_id, Comment.comment_pid,
                                      Comment.comment_regdate, Comment.user_id,
                                      (treeQuery.c.depth + 1).label('depth'),
                                      func.concat(treeQuery.c.lvl,'-', Comment.comment_id).label('lvl'),
                                      func.concat(treeQuery.c.lvl2,'-', func.lpad(Comment.comment_id, 10, '0').cast(VARCHAR(10000))).label('lvl2')
                                      ).\
                        join(treeQuery, Comment.comment_pid==treeQuery.c.comment_id)

    recursiveQuery = treeQuery.union(uniTreeQuery)

    result = session.query(recursiveQuery).\
                with_entities(recursiveQuery.c.board_id.label('board_id'),
                              recursiveQuery.c.board_list_id.label('board_list'),
                              recursiveQuery.c.comment_content.label('comment_content'),
                              recursiveQuery.c.comment_del.label('comment_del'),
                              recursiveQuery.c.comment_id.label('comment_id'),
                              recursiveQuery.c.comment_pid.label('comment_pid'),
                              recursiveQuery.c.comment_regdate.label('comment_regdate'),
                              recursiveQuery.c.depth.label('depth'),
                              recursiveQuery.c.user_id.label('user_id'),
                              recursiveQuery.c.lvl.label('lvl'),
                              recursiveQuery.c.lvl2.label('lvl2')
                ).\
                order_by('lvl2')

    resultVal = convertStatementToList(result)
    return resultVal

# def getComment(data):
    
#     query = """
#             with recursive cte as
#             (
#              select     board_id,
#              				board_list_id,
#              				comment_id,
#              				comment_pid,
#              				comment_content,
#              				comment_del,
#              				user_id,
#              				comment_regdate,
             				            
#                         0 AS depth,
#                         CAST(comment_id AS VARCHAR(1000)) as lvl,
#                         CAST(LPAD(comment_id, 10, "0") AS VARCHAR(1000)) as lvl2
#             from       comment
#             where      board_id = :boardId AND board_list_id = :boardListId AND comment_pid = 0
#             union all
#             SELECT    r.board_id,
#              				r.board_list_id,
#              				r.comment_id,
#              				r.comment_pid,
#              				r.comment_content,
#              				r.comment_del,

#              				r.user_id,
#              				r.comment_regdate,
                        
#                         1 + depth AS depth,
#                         CONCAT(cte.lvl, "-", r.comment_id) as lvl,
#                         CONCAT(cte.lvl2, "-", LPAD(r.comment_id, 10, "0")) as lvl2
#             from       comment r

#              inner join cte
#             on r.comment_pid = cte.comment_id

#             WHERE		r.board_id = :boardId AND r.board_list_id = :boardListId
# 	        )       
#             SELECT * FROM cte   
#             ORDER BY lvl2;
#             """
#     stmt = text(query)
#     stmt = stmt.bindparams(bindparam("boardId", type_=Integer), bindparam("boardListId", type_=String))
#     result = session.execute(stmt, {"boardId": int(data['boardId']), "boardListId": data['boardListId']})

#     resultVal = convertStatementToList2(result)

#     return resultVal


# 댓글 삭제
def delComment(data):
    updateContent = {}
    updateContent['comment_regdate'] = datetime.datetime.now()
    updateContent['comment_del'] = 1

    result = session.query(Comment).\
            filter(Comment.comment_id == data['commentId']).\
            update(updateContent, synchronize_session='fetch')
    
    session.commit()

    resultVal = returnCodeAfterUpdate(result)
    return resultVal

