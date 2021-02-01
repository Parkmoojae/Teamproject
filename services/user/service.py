from datasource import *
from sqlalchemy import text, exc, and_, or_, func, String, DateTime
import uuid, datetime
from ainUtil import *
from dto import *

    # from dto.User import *
def userInsert(data):
    print(data)
    resultCode = '500'
    user = model.User(user_id= data['userId'],
                user_pw = data['userPw']
            )
    # user = User(str(uuid.uuid4()), 
    #             AUTH_TYPE = False,
    #             USER_ID = data['userId'], 
    #             USER_PW=data['userPw'], 
    #             USER_EMAIL=data['userEmail'],
    #             USER_PHONE = data['userPhone'], 
    #             USER_SEX=data['userSex'], 
    #             USER_BDAY=data['userBirth'],
    #             USER_ADD = data['userAdd'], 
    #             USER_REG=datetime.datetime.now(),
    #             USER_DELETE=False)
    # try:
    #     session.add(user)
    #     session.commit()
    #     resultCode = '200'
    # except exc.IntegrityError:
    #     resultCode = "500"

    try:
        session.add(user)
        session.commit()
        resultCode = '200'
    except:
        session.rollback()
        resultCode = '500'
        raise
    finally:
        session.close()  # optional, depends on use case


    print("########")
    print(resultCode)
    print("########")
    
    return resultCode

def userLogin(data):
    queryResult = session.query(model.User).\
        with_entities(
            model.User.user_id, model.User.user_pw, model.User.user_group_id
        ).\
                    filter(model.User.user_id==data['userId'])
    
    result = queryToDict(queryResult)
    print(result)

    return result