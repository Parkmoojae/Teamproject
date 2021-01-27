from datasource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime
import uuid, datetime
from dto import *

def userLogin(data):
    queryResult = session.query(model.User).\
                    filter(model.User.user_id==data['userId'])
    
    result = queryResult.all()
    print(result)
    return result