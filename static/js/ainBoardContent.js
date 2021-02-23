console.log(contentData['nowPageNum'])
console.log(contentData['resultDB'][0])

// 변수선언
// 변수선언-게시판 헤더(종류표기)
let cardHeader = document.getElementById('cardHeader')
let spanTag = document.createElement("span")
// 변수선언-게시글 제목
let contentTitle = document.getElementById('contentTitle')
// 변수선언-작성자
let contentWriter = document.getElementById('contentWriter')
// 변수선언-작성일
let contentRegDate = document.getElementById('contentRegDate')
// 변수선언-내용
let content = document.getElementById('content')
// 변수선언-댓글 내용
let commentContent = document.getElementById('commentContent')
// 변수선언-클릭한 대댓글의 userId
let clickedId = null
// 변수선언-클릭한 댓글의 id(대댓글의 pid)
let clickedComPId = null

// 게시글 값 넣기
setContent(contentData)

// 댓글 값 넣기
setComment(contentData)


// 수정버튼 클릭 이벤트
document.getElementById('conModiBtn').addEventListener('click', (e)=>{
    let data={}
    data['nowPageNum'] = contentData['nowPageNum']
    data['boardListId'] = contentData['resultDB'][0]['board_list_id']
    data['boardId'] = contentData['resultDB'][0]['board_id']
    data['title'] = contentTitle.value
    data['writer'] = contentData['resultDB'][0]['user_id']
    data['regDate'] = contentRegDate.value
    data['content'] = content.value
    console.log(data)
    location.href="/render/board/update?board_list_id=" + data['boardListId'] + "&board_id=" + data['boardId']
    
})

// 삭제버튼 클릭 이벤트
document.getElementById('conDelBtn').addEventListener('click', (e)=>{
    let data={}
    data['nowPageNum'] = contentData['nowPageNum']
    data['board_list_id'] = contentData['resultDB'][0]['board_list_id']
    data['board_id'] = contentData['resultDB'][0]['board_id']
    data['writer'] = contentData['resultDB'][0]['user_id']
    console.log(data)
    delContent(data)
    
})

// 답글버튼 클릭 이벤트
document.getElementById('conWriteBtn').addEventListener('click', (e)=>{
    let data={}
    data['nowPageNum'] = contentData['nowPageNum']
    data['boardListId'] = contentData['resultDB'][0]['board_list_id']
    data['boardId'] = contentData['resultDB'][0]['board_id']
    data['title'] = contentTitle.value
    data['writer'] = contentData['resultDB'][0]['user_id']
    data['regDate'] = contentRegDate.value
    data['content'] = content.value
    console.log(data)
    location.href='/render/board/write?board_list_id=' + data['boardListId'] + '&board_pid=' + data['boardId']
})

// 댓글작성(입력) 버튼 클릭 이벤트
document.getElementById('commentWriteBtn').addEventListener('click', (e)=>{
    // 댓글 content null값 확인
    if(commentContent.value==''){
        alert('댓글을 입력해주세요')
    }
    else{
        let data={}
        data['contentWriter'] = contentWriter.value
        data['commentContent'] = commentContent.value
        data['nowPageNum'] = contentData['nowPageNum']
        data['boardListId'] = contentData['resultDB'][0]['board_list_id']
        data['boardId'] = contentData['resultDB'][0]['board_id']
        // data['commentPid'] = null
        data['commentPid'] = clickedComPId
        console.log(data)
        
        insertCommnet(data)
        
        // 댓글창 초기화
        commentInit()
        // commentContent.value = ""
    }
})

// 댓글 선택한 id 기억(대댓글 작성을 위해 해당 댓글의 comment_id값 저장)
document.getElementById('commentAll').addEventListener('click', (e)=>{
    if(e.target.matches('span')){
        clickedId = e.target.parentNode.parentNode.firstChild.nextSibling.value
        clickedComPId = e.target.parentNode.parentNode.firstChild.value
        document.getElementById('commentPid').innerHTML = '<label id=label>' + clickedId + '에 댓글' + '<input type="button" id="removeClickedId" value="X"></lable>' 
                                                            // '<input type="hidden" id="hiddenClickedId value="' + clickedId + '"/>'

    }
    else{
        // 댓글창 초기화
        commentInit()
    }
})

// 댓글 선택한 id 옆에 x 버튼 이벤트(대댓글의 pid값 표기 삭제 이벤트)
document.querySelector('#commentPid').addEventListener('click', (e)=>{
    if(e.target.matches('#removeClickedId')){
        // 댓글창 초기화
        commentInit()
    }
})
// 댓글창 초기화
function commentInit(){
    temp = document.getElementById('commentPid').lastChild
        let newSpan = document.createElement('span')
        temp.parentNode.replaceChild(newSpan, temp)
        clickedId = null
        clickedComPId = null
        document.getElementById('commentPid').innerHTML = "<label>내용</label>"
        commentContent.value = ""
}


// 댓글 삭제 버튼 이벤트
document.getElementById('commentAll').addEventListener('click', (e)=>{
    if(e.target.matches('button')){
        let commentId = e.target.parentNode.parentNode.firstChild.firstChild.value
        let writerId = e.target.parentNode.parentNode.firstChild.firstChild.nextSibling.value
        // alert(writerId)
        let data={}
        data['nowPageNum'] = contentData['nowPageNum']
        data['boardListId'] = contentData['resultDB'][0]['board_list_id']
        data['boardId'] = contentData['resultDB'][0]['board_id']
        data['commentContent'] = commentContent.value
        data['commentPid'] = null
        data['userId'] = writerId
        data['commentId'] = commentId
        delComment(data)

    }
})





// 게시글 값 넣기
function setContent(data){
    console.log(data)
    // 게시글-게시판 종류 넣기
    let boardName = ''
    if(data['resultDB'][0]['board_list_id']=="1"){
        boardName = '자유'
    }
    if(data['resultDB'][0]['board_list_id']=="2"){
        boardName = '취미'
    }
    
    document.getElementById('boardName').innerText = boardName

    spanTag.innerHTML = boardName + "게시판"
    cardHeader.appendChild(spanTag)
    
    // 게시글-제목 넣기
    contentTitle.value = data['resultDB'][0]['board_title']
    
    // 게시글-작성자 넣기
    contentWriter.value = data['resultDB'][0]['user_id']
    
    
    // //게시글-작성일 넣기
    contentRegDate.value = data['resultDB'][0]['board_regdate']
    
    
    //게시글-내용 넣기
    content.value = data['resultDB'][0]['board_content']

}

// 댓글 리스트 넣기
function setComment(data){
    let commentAll = document.getElementById('commentAll')
    let divComment = document.createElement('div')


    // 댓글 초기화
    let temp = document.getElementById("commentAll").lastChild
    let newTd = document.createElement('td')
    temp.parentNode.replaceChild(newTd, temp)


    for(i=0; i<data['commentList']['data'].length; i++){

        // 댓글 삭제 시
        let commentCon = data["commentList"]["data"][i]["comment_content"]
        let delButton = '<button type="button" class="btn btn-block btn-default">삭제</button>'
        if(data['commentList']['data'][i]['comment_del']==1){
            commentCon = "삭제된 댓글입니다."
            // delButton = '<span type="text" class="form-control" style="text-align: center;">삭제 완료</span>'
            delButton = '<button type="button" class="btn btn-block btn-default" disabled>삭제</button>'
        }
        
        

        //depth에 따른 re 표기
        let reCount = ''
        if(data['commentList']['data'][i]['depth']>0){
            for(j=0; j<data['commentList']['data'][i]['depth']; j++){
                reCount = reCount + 're:'
            }
        }

        let divRow = document.createElement('div')
        divRow.setAttribute('class', 'row')
        let commentRow ='<div class="col-sm-10">' + 
                        '<input type=hidden value=' + data["commentList"]["data"][i]["comment_id"] + '>' +
                        '<input type=hidden value=' + data["commentList"]["data"][i]["user_id"] + '>' +
                        '<div class="input-group mb-3">' +
                            '<div class="input-group-prepend">' +
                                '<span class="input-group-text">' + reCount + ' ' + data["commentList"]["data"][i]["user_id"] + '</span>' +
                            '</div>' +
                            '<span type="text" class="form-control">' + commentCon + 
                            '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' + 
                            data["commentList"]["data"][i]["comment_regdate"] + 
                            '</span>' +
                        '</div>' +
                        '</div>'
        
        let buttonDel = '<div class="col-sm-2">' +
                        delButton + 
                        '</div>'

        divRow.innerHTML = commentRow + buttonDel
        // commentAll.appendChild(divRow)
        divComment.appendChild(divRow)
        
    }
    commentAll.appendChild(divComment)
    // commentDiv.innerHTML = commentList
    // commentDiv2.innerHTML = btnList
    
}



// 게시글 삭제
function delContent(bodyData){
    let rootUrl = 'http://127.0.0.1:5000';
    let routing = '/board/delete';
    fetch(rootUrl + routing, {
        method : 'POST',
        headers : {
            'Content-type' : 'application/json;charset=utf-8'
        },
        body : JSON.stringify(bodyData)
    })
    .then(response => {
        console.log(response); 
        return response.json();
    })
    .then(res=>{
        if(res['code']==22){
            alert("권한없음")
        }
        if(res['code']==1){
            alert("삭제완료")
            location.href='/board?board_list_id=' + bodyData['board_list_id'] +'&nowPageNum=' + bodyData['nowPageNum']
        }
    })

}


// 댓글 DB 입력
function insertCommnet(bodyData){
    console.log(bodyData)
    let rootUrl =  'http://127.0.0.1:5000';
    let routing = '/insertComment'
    fetch(rootUrl + routing, {
        method : 'POST',
        headers : {
            'Content-type' : 'application/json;charset=utf-8',
        },
        // headers : {},
        body : JSON.stringify(bodyData)
        // body: blob
    })  
    .then(response => {console.log(response); return response;})
    .then(function(temp){
        return temp.json();
    })
    .then(function(res){
        // 데코레이터 권한 체크
        if(res['code']==22){
            alert('권한이 없습니다.')
        }
        if(res['resultDB']['code']==1){
            console.log(res)
            setComment(res)
            alert("댓글 입력 완료")
        }
        else{
            console.log(res)
            alert("댓글 입력 실패")
        }
    })
}

// 댓글 DB 삭제
function delComment(bodyData){
    let rootUrl =  'http://127.0.0.1:5000';
    let routing = '/delComment'
    fetch(rootUrl + routing, {
        method : 'POST',
        headers : {
            'Content-type' : 'application/json;charset=utf-8',
        },
        body : JSON.stringify(bodyData)
        // body: blob
    })  
    .then(response => {console.log(response); return response;})
    .then(function(temp){
        return temp.json();
    })
    .then(function(res){
        if(res['code']==22){
            alert("권한이 없습니다.")
        }
        if(res['resultDB']['code']==1){
            console.log(res)
            setComment(res)
            alert("댓글 삭제 완료")
        }
        else{
            console.log(res)
            alert("댓글 삭제 실패")
        }
    })
}