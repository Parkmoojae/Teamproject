
let board_list_id = get_query()['board_list_id'];
if(board_list_id==undefined){
    board_list_id = get_boardListId();
}
if(board_list_id==1){
    document.getElementById('freeBoard').classList.toggle("active");
}else if(board_list_id==2){
    document.getElementById('hobbyBoard').classList.toggle("active");
}else if(board_list_id==3){
    document.getElementById('adminBoard').classList.toggle("active");
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


function get_boardListId(){
    let uri = document.location.href;
    let boardListId = uri.split('/')[5];
    
    return boardListId
}
function get_query(){
    var url = document.location.href;
    var qs = url.substring(url.indexOf('?') + 1).split('&');
    for(var i = 0, result = {}; i < qs.length; i++){
        qs[i] = qs[i].split('=');
        result[qs[i][0]] = decodeURIComponent(qs[i][1]);
    }
    return result;
};