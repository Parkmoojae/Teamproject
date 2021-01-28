
from sqlalchemy import exc
import datetime
from pytz import timezone, utc

def convertStatementToList(statement):
    result = {}
    dataList = []
    rows = statement.all()

    for row in rows:
        dataList.append(row._asdict())

    result['data'] = dataList
    return result

# sql 직접 사용시에..
def convertStatementToList2(data):
    result = {}
    dataList = [{column: value for column, value in rowproxy.items()} for rowproxy in data]
    result['data'] = dataList
    return result

def sessionAdd(dataObject, session):
    result = {}
    try:
        session.add(dataObject)
        session.commit()
        result['code'] = '1'
    except exc.IntegrityError as e:
        print(e)
        session.rollback()
        result['code'] = '0'
    return result

def returnCodeAfterUpdate(resultCount):
    result = {}
    if resultCount>=1:
        result['code']='1'
    else:
        result['code']='0'
    return result
    
def getCurrentDateTime():
    currentUtcNaiveTime = datetime.datetime.utcnow()
    return utc.localize(currentUtcNaiveTime)

def convertUtcTimeToLocalTime(dt, **kwargs):
    targetTimezone = None
    if kwargs.get('timezone', None) is None:
        targetTimezone = timezone('Asia/Seoul')
    if dt.tzinfo is None:
        return utc.localize(dt).astimezone(targetTimezone)
    else:
        return dt.astimezone(targetTimezone)