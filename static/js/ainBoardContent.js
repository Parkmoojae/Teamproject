console.log(contentData['nowPageNum'])
console.log(contentData['resultDB'][0])
// 게시판 값 넣기
setContent(contentData)


// 게시판 값 넣기
function setContent(data){
    console.log(data)
    // 게시글-게시판 종류 넣기
    let cardHeader = document.getElementById('cardHeader')
    let spanTag = document.createElement("span")
    spanTag.innerHTML = data['resultDB'][0]['board_list_id']+"번 게시판"
    cardHeader.appendChild(spanTag)

    // 게시글-제목 넣기
    let contentTitle = document.getElementById('contentTitle')
    contentTitle.value = data['resultDB'][0]['board_title']

    // 게시글-작성자 넣기
    let contentWriter = document.getElementById('contentWriter')
    contentWriter.value = data['resultDB'][0]['user_id']
  

    // //게시글-작성일 넣기
    let contentRegDate = document.getElementById('contentRegDate')
    contentRegDate.value = data['resultDB'][0]['board_regdate']


    //게시글-내용 넣기
    let content = document.getElementById('content')
    content.value = data['resultDB'][0]['board_content']

    
}

