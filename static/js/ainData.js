nowPageNum = 1
// 게시글 클릭시 content로 이동
document.getElementById("example2").addEventListener('click', (e)=>{
    if(e.target.matches('td')){
        boardId = 8
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

    })
}