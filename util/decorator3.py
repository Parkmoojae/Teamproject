from services.board import service as boardService
from services.auth import service as authService
from flask import session as flaskSession
from flask import request, redirect
from functools import wraps

def kys_authDecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        invalidRequestFlag = 0
        insufficientAuthorityFlag = 0
        notAllowedFlag = 0

        requestPath = request.path
        currentUserData = flaskSession.get('loginUserData')
        # print('currentUserData : ', currentUserData)
        currentUserAuthority =  authService.authority_groupAuthority_getList(currentUserData)
        pathVariableList = requestPath.split('/')

        try:
            del pathVariableList[0]

            print('check kys_authDecorator ===== start =====')
            print('check requestPath(kys_authDecorator) :', requestPath)
            print('userData : ', flaskSession.get('loginUserData'))
            print('currentUserAuthority : ', currentUserAuthority)        
            print('requestPath pathVariable[0] : ',  requestPath.split('/')[1])

            # testUrl 체크
            if(pathVariableList[0] == 'test'):
                print('testing ...')

            # rendering 권한 체크
            if(pathVariableList[0] == 'render'):
                print('rendering ...')
                print(pathVariableList)
                if(pathVariableList[1] == 'board'):
                    if(pathVariableList[2] == 'write'):
                        requiredArgList = ['board_list_id']
                        requestArgList = request.args.to_dict()
                        # requiredArgList에 있는 인자가 들어오지 않으면 화면이동 X
                        for requiredArg in requiredArgList:
                            if requiredArg not in requestArgList.keys():
                                invalidRequestFlag = 1
                        if(currentUserAuthority[requestArgList['board_list_id']]['auth_board_write'] != 1 ):
                            print('redirect ...')
                            insufficientAuthorityFlag = 1                                
                        
                    if(pathVariableList[2] == 'update'):
                        requiredArgList = ['board_list_id', 'board_id']
                        requestArgList = request.args.to_dict()
                        # requiredArgList에 있는 인자가 들어오지 않으면 화면이동 X
                        for requiredArg in requiredArgList:
                            if requiredArg not in requestArgList.keys():
                                invalidRequestFlag = 1
                        print(requestArgList)
                        boardContent = boardService.board_getContent(requestArgList)
                        print('boardContent : ', boardContent)
                        contentOwner = boardContent['data'][0]['user_id']
                        print('contentOwner : ', contentOwner)
                        if( (currentUserAuthority[requestArgList['board_list_id']]['auth_board_modi'] != 1) and (currentUserData['user_id'] !=  contentOwner) ):
                            print('redirect ...')
                            insufficientAuthorityFlag = 1                                
            # data 처리
            if(pathVariableList[0] == 'board'):
                print('data processing ...')
                resultData = {}
                requestData = request.get_json()
                if(pathVariableList[1] == 'write'):
                    if (currentUserAuthority[requestData.get('board_list_id', None)]['auth_board_write'] != 1):
                        resultData['code'] = 22
                        resultData['description'] = 'insufficient authority'
                if(pathVariableList[1] == 'update'):
                    boardContent = boardService.board_getContent(requestData)
                    print('boardContent : ', boardContent)
                    contentOwner = boardContent['data'][0]['user_id']
                    print('contentOwner : ', contentOwner)                    
                    if ( (currentUserAuthority[requestData.get('board_list_id', None)]['auth_board_modi'] != 1) and (currentUserData['user_id'] !=  contentOwner) ):
                        resultData['code'] = 22
                        resultData['description'] = 'insufficient authority'                    
                if(pathVariableList[1] == 'delete'):
                    boardContent = boardService.board_getContent(requestData)
                    print('boardContent : ', boardContent)
                    contentOwner = boardContent['data'][0]['user_id']
                    print('contentOwner : ', contentOwner)                    
                    if ( (currentUserAuthority[requestData.get('board_list_id', None)]['auth_board_del'] != 1) and (currentUserData['user_id'] !=  contentOwner) ):
                        resultData['code'] = 22
                        resultData['description'] = 'insufficient authority'    

            if notAllowedFlag == 1:
                pass
            if invalidRequestFlag == 1:
                print('invalidRequestFlag = 1 ...')
                return redirect('/render/invalidRequest')
            if insufficientAuthorityFlag == 1:
                print('insufficientAuthorityFlag = 1 ...')
                return redirect('/render/insufficientAuthority')
            print('check kys_authDecorator =====  end  =====')
        except Exception as ex:
            print('exception !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', ex)
        return func(*args, **kwargs)
    return wrapper