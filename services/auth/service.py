from datasource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime
from dto import model
from util import *

def authority_groupAuthority_getList(data):
    result = {}
    print('data service(authority_groupAuthority_getList) : ', data)
    rows = session.query(model.Auth)\
            .join(model.User, model.Auth.user_group_id == model.User.user_group_id)\
            .with_entities(
                model.User.user_id,
                model.User.user_group_id,
                model.Auth.auth_id,
                model.Auth.board_list_id,
                model.Auth.auth_board_write,
                model.Auth.auth_board_del,
                model.Auth.auth_board_modi,
                model.Auth.auth_board_read,
                model.Auth.auth_comment_write,
                model.Auth.auth_comment_del
            ).filter(model.User.user_group_id == data['user_group_id'])
    
    for row in rows:
        tempDict = row._asdict()
        result[tempDict['board_list_id']]=tempDict
    return result

    