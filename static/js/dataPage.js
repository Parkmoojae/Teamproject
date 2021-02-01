
createBoard(resultList['boardList']);
let board_list_id = get_query()['board_list_id'];
if(board_list_id==undefined){
    board_list_id=1;
}


document.getElementById('freeBoard').addEventListener('click', (e)=>{
    board_list_id = 1;
    location.href="/board?board_list_id="+board_list_id;
});

document.getElementById('hobbyBoard').addEventListener('click', (e)=>{
    board_list_id = 2;
    location.href="/board?board_list_id="+board_list_id;

});

document.getElementById('adminBoard').addEventListener('click', (e)=>{
    board_list_id = 3;
    location.href="/board?board_list_id="+board_list_id;

});


document.getElementById('example1').addEventListener('click',(e)=>{
    if(e.target.matches('td')){
        if(e.target.parentNode.firstChild.nextElementSibling.innerText == 0){
        let board_id = e.target.parentNode.firstChild.innerText;
        let nowPageNum = document.querySelector('#example1_paginate > ul > li.paginate_button.page-item.active > a').innerText;
        
        location.href="/getBoardContent/"+board_id+'/'+board_list_id+'/'+nowPageNum;
        }
    }
});

document.getElementById('writeBoard').addEventListener('click',(e)=>{
    location.href="/render/board/write?board_list_id="+board_list_id;
});



function createBoard(boardList){
    
    
    
    
    let tbody= document.getElementById('example1tbody');

    for(var i=0; i<boardList.length;i++){
    
    if(boardList[i]['depth']>0){
        for(var j=0; j<boardList[i]['depth'];j++){
            boardList[i]['board_title']="→"+boardList[i]['board_title'];
            
        }
    }        
    let tr = document.createElement('tr');

    if(boardList[i]['board_del']==1){
        boardList[i]['board_title']="삭제된 게시글입니다.";
        let del = document.createElement('td');
        del.innerText = boardList[i]['board_title'];
        del.colSpan=4;
    }
    
    let bId = document.createElement('input');
    let bNum = document.createElement('td');
    let bWriter = document.createElement('td');
    let bTitle = document.createElement('td');
    let bDate = document.createElement('td');
    let bDel = document.createElement('input');
    bDel.id = "boardDel";
    bDel.type = "hidden";

    bId.id = "boardId";
    bId.type = "hidden";

    bDel.innerText = boardList[i]['board_del'];
    bId.innerText = boardList[i]['board_id'];
    bNum.innerText = boardList[i]['b_num'];
    bWriter.innerText = boardList[i]['user_id'];
    bTitle.innerText = boardList[i]['board_title'];
    bDate.innerText = boardList[i]['board_regdate'];
    
    tr.appendChild(bId);
    tr.appendChild(bDel);
    tr.appendChild(bNum);
    tr.appendChild(bWriter);
    tr.appendChild(bTitle);
    tr.appendChild(bDate);

    tbody.appendChild(tr);


    }
    

}

function get_query(){
    var url = document.location.href;
    var qs = url.substring(url.indexOf('?') + 1).split('&');
    for(var i = 0, result = {}; i < qs.length; i++){
        qs[i] = qs[i].split('=');
        result[qs[i][0]] = decodeURIComponent(qs[i][1]);
    }
    return result;
}