nowPageNum = 1
document.getElementById("example2").addEventListener('click', (e)=>{
    if(e.target.matches('td')){
        alert("!!!!!")
        boardId = 1
        boardListId = "1"
        // bodyData = {}
        // bodyData['boardListId'] = boardListId
        // bodyData['boardId'] = boardId
        // bodyData['nowPageNum'] = nowPageNum
        // sendData(bodyData)
        location.href = '/getBoardContent/' + boardId + '/' + boardListId + '/' + nowPageNum
    }
})



function sendData(bodyData){
    console.log(bodyData)
    let rootUrl =  'http://127.0.0.1:5000';
    let routing = '/getBoardContent'
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
        console.log(temp)
        // temp2 = temp.json()
        // console.log(temp2)
        // console.log(temp2['resultDB'])
        return temp.json();
    })
    .then(function(res){
        console.log(res)
        console.log(res['resultDB'][0])
        location.href = "/render/boardContent/" + res['resultDB'][0] + '/' + res['nowPageNum']
    //     // if(res["resultDB"]=='0'){
    //     //     console.log("로그인 실패: 아이디 불일치")
    //     //     alert("아이디가 불일치 합니다.")

    //     // }else if(res["resultDB"]=='1'){
    //     //     console.log("로그인 성공")
    //     //     // location.href = '/board/boardcommon'
    //     //     // location.href = '/render/main'
    //     //     data1 = "boadId"
    //     //     pageNum = 1
    //     //     location.href = '/board/post/'+ data1 + "/" + pageNum

    //     // }else if(res["resultDB"]=='-1'){
    //     //     console.log("로그인 실패: 비밀번호 불일치")
    //     //     alert("비밀번호가 다릅니다.")
    //     // }

    })
}