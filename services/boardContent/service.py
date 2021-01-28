from datasource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime
import uuid, datetime
from dto.model import Board
from ainUtil import *


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