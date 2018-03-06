$(document).ready(function () {
    search_pmp('get');
})


function search_pmp(method) {
    $('tbody').empty();
    if(method ==='get' ){
        $.ajax({
            type: 'get',
            url: '/pmp/searchpmpkeywordslist/',
            success:function (data) {
                $.each(JSON.parse(data), function (index, content) {
                    createElement(content)
                })
            }
        })
    }else if(method === 'post'){
        search_text = $('.search_text').val();
        if(search_text.length ===0 ){
            alert('请输入搜索关键字');
        }else{
            $.ajax({
                type: 'post',
                url: '/pmp/searchpmpkeywordslist/',
                data: $('form').serialize(),
                success:function (data) {
                    console.log(data.length);
                    $.each(JSON.parse(data), function (index, content) {
                        createElement(content)
                    })
                }
            })
        }


    }else{

    }


}