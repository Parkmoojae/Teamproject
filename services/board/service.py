from datasource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime
from dto import model
from util import *

def test_list(data):
    result = {}
    result = session.query(model.Board)\
            .with_entities(
                model.Board.board_id, model.Board.board_pid, model.Board.board_list_id, 
                model.Board.user_id, model.Board.board_title, model.Board.board_content, 
                model.Board.board_regdate, model.Board.board_del
            )
    return convertStatementToList(result)

def board_getContent(data):
    result = {}
    result = session.query(model.Board)\
        .with_entities(
            model.Board.board_id, model.Board.board_pid, model.Board.board_list_id, 
            model.Board.user_id, model.Board.board_title, model.Board.board_content, 
            model.Board.board_regdate, model.Board.board_del
        ).filter(model.Board.board_id == data['board_id'])
    return convertStatementToList(result)

def board_write(data):
    result = {}
    board = model.Board(
        board_content = data.get('board_content', None), user_id = data.get('user_id', None), board_regdate = getCurrentDateTime(),
        board_del = 0, board_list_id = data.get('board_list_id', None), board_title = data.get('board_title', None),
        board_pid = data.get('board_pid', 0)
    )
    # board = model.Board(**data)
    return sessionAdd(board, session)

def board_update(data):
    result = {}
    result = session.query(model.Board)\
        .filter(model.Board.board_id==data['board_id'])\
        .update(data, synchronize_session='fetch')	
    session.commit()
    return returnCodeAfterUpdate(result)

def board_delete(data):
    result = {}
    result = session.query(model.Board)\
        .filter(model.Board.board_id==data['board_id'])\
        .update({"board_del":1}, synchronize_session='fetch')	
    session.commit()
    return returnCodeAfterUpdate(result)    