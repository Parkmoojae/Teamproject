console.log(contentData['nowPageNum'])
console.log(contentData['resultDB'][0])
setContent(contentData)


function setContent(contentData){
    // 게시글-게시판 종류 달기
    let cardHeader = document.getElementById('cardHeader')
    let spanTag = document.createElement("span")
    spanTag.innerHTML = contentData['resultDB'][0]['board_list_id']+"번 게시판"
    cardHeader.appendChild(spanTag)
}

