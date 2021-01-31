
createBoard(resultList['boardList']);


document.getElementById('freeBoard').addEventListener('click', (e)=>{
    let board_list_id = 1;
    location.href="/board?board_list_id="+board_list_id;
});

document.getElementById('hobbyBoard').addEventListener('click', (e)=>{
    let board_list_id = 2;
    location.href="/board?board_list_id="+board_list_id;

});

document.getElementById('adminBoard').addEventListener('click', (e)=>{
    let board_list_id = 3;
    location.href="/board?board_list_id="+board_list_id;

});

/*     
function fetchBoard(b_list_id){
    fetch("/board", {
        method: "POST",
        headers:{
            "Content-Type" : "application/json",
        },
        body : JSON.stringify({
            board_list_id : b_list_id
        })
    }).then((res) => {

    });
} */

//테이블초기화

/* function tableClean(){
    
   let example1tbody = document.getElementById('example1tbody');
   while(example1tbody.hasChildNodes){
    example1tbody.removeChild(example1tbody.firstChild);
   }
} */


function createBoard(boardList){
    
    
    //tableClean(); 
    
    let tbody= document.getElementById('example1tbody');

    for(var i=0; i<boardList.length;i++){
        
    let tr = document.createElement('tr');
    let bNum = document.createElement('td');
    let bWriter = document.createElement('td');
    let bTitle = document.createElement('td');
    let bDate = document.createElement('td');

    

    bNum.innerText = boardList[i]['b_num'];
    bWriter.innerText = boardList[i]['user_id'];
    bTitle.innerText = boardList[i]['board_title'];
    bDate.innerText = boardList[i]['board_regdate'];
    
    tr.appendChild(bNum);
    tr.appendChild(bWriter);
    tr.appendChild(bTitle);
    tr.appendChild(bDate);

    tbody.appendChild(tr);

    }
    

}

