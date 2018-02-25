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
        $.ajax({
            type: 'post',
            url: '/pmp/searchpmpkeywordslist/',
            data: $('form').serialize(),
            success:function (data) {
                $.each(JSON.parse(data), function (index, content) {
                    createElement(content)
                })
            }
        })
    }else{

    }


}



function createElement(content) {

    var vtr = $('<tr></tr>');
    $('tbody').append(vtr);

    var td_longEN = $('<td></td>');
    td_longEN.text(content.long_EN);
    td_longEN.appendTo(vtr);

    var td_shortEN = $('<td></td>');
    td_shortEN.text(content.short);
    td_shortEN.appendTo(vtr);

    var td_longCN = $('<td></td>');
    td_longCN.text(content.long_CN);
    td_longCN.appendTo(vtr);

    var td_desc = $('<td></td>');
    td_desc.text(content.description);
    td_desc.appendTo(vtr);

}