// 이벤트 리스너
document.querySelector('body').addEventListener('click', function(e){
    eventTarget = e.target;
    // 작성버튼 이벤트
    if (eventTarget.matches('#btn_boardWrite')){
        // console.log('작성버튼 클릭');
        process_boardWrite();
    }else if(eventTarget.matches('#btn_cancel')){
        // console.log('취소버튼 클릭');
        location.href='/render/tempPage'
    }
});

async function process_boardWrite(){
    fetchDataObject = {};
    fetchDataObject['board_pid'] = document.querySelector('#board_pid').value;
    fetchDataObject['board_list_id'] = document.querySelector('#board_list_id').value;
    fetchDataObject['board_title'] = document.querySelector('#board_title').value;
    fetchDataObject['board_content'] = document.querySelector('#board_content').value;

    fetchDataObjectKeyList = Object.keys(fetchDataObject);

    for(var i=0; i< fetchDataObjectKeyList.length; i++){
        var value = fetchDataObject[fetchDataObjectKeyList[i]];
        if ( value == '' || value == null){
            delete fetchDataObject[fetchDataObjectKeyList[i]];
        }
    }
    // console.log(fetchDataObject);

    fetchData = await myFetch('/board/write', {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },
        body:JSON.stringify(fetchDataObject)
    });
    console.log('fetchData : ', fetchData);
    if(fetchData['code'] == '1'){
        location.href = '/render/tempPage';
    }
}

async function myFetch(fetchUrl, requestObject){
    data = await fetch(fetchUrl, requestObject).then( (res) => res.json());
    return data;
}