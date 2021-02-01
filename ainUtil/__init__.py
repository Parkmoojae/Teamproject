import time
import datetime

def resultToDict(statement):
    resultVal = [{column: value for column, value in rowproxy.items() }for rowproxy in statement]
    return resultVal

def queryToDict(queryResult):
    result = []
    rows = queryResult.all()

    for row in rows:
        result.append(row._asdict())
        
    return result


# 현재시간
def nowTime():
    operationTime = time.localtime()
    operationTime = "%04d/%02d/%02d %02d:%02d:%02d" % (operationTime.tm_year, operationTime.tm_mon, operationTime.tm_mday, operationTime.tm_hour, operationTime.tm_min, operationTime.tm_sec)
    return operationTime

def timeFormat(time):
    result = time.strftime('%Y-%m-%d %H:%M:%S')
    return result

def commentTimeFormat(datas):
    # datas = result['commentList']['data']
    for i in range(len(datas)):
        commentTime = timeFormat(datas[i]['comment_regdate'])
        datas[i]['comment_regdate'] = commentTime
    return datas