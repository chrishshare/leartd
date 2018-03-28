//首次进入、刷新页面时默认加载url列表
$(document).ready(function () {
    getUrls('get');
    getClassify('index');
    getClassify('addurl');
})


//创建url列表相关元素
function createUrlsElement(content) {
    var urls = $('<div></div>');
    urls.addClass("col-sm-3 urls");
    $('.row').append(urls);

    var panel = $('<div></div>');
    panel.addClass("panel panel-info");
    $(panel).appendTo(urls);

    var panelHeader = $('<div></div>');
    panelHeader.addClass("panel-heading");
    panelHeader.text(content.classify__type_name);
    $(panelHeader).appendTo(panel);

    var panelBody = $('<div></div>');
    panelBody.addClass("panel-body");
    $(panelBody).appendTo(panel);

    var panelBody_a = $('<a></a>');
    panelBody_a.attr("href", content.url_link);
    panelBody_a.addClass('urls_link');
    panelBody_a.text(content.url_name);
    $(panelBody_a).appendTo(panelBody);

    var panelFooter = $('<div></div>');
    panelFooter.addClass("panel-footer");
    $(panelFooter).appendTo(panel);

    var panelFooter_p = $('<p></p>');
    $(panelFooter_p).appendTo(panelFooter);

    var panelFooter_delimg = $('<img>');
    panelFooter_delimg.addClass("delete");
    panelFooter_delimg.attr({"src":"static/icon/delete16.png"});
    $(panelFooter_delimg).appendTo(panelFooter_p);

}


//从后台获取url列表，并显示
function getUrls(type) {
    $('.row').empty();
    if(type === 'get'){
        $.ajax({
            type: 'get',
            url: '/geturls/',
            success: function (data) {
                html = '';
                $.each(JSON.parse(data), function (index, content) {
                        createUrlsElement(content);
                    });
                waterfall();
            },
        });
    }else if(type === 'post'){
        $.ajax({
            type: 'post',
            url: '/geturls/',
            data: $('.search-from').serialize(),
            success: function (data) {
                html = '';
                $.each(JSON.parse(data), function (index, content) {
                    createUrlsElement(content);
                });
                waterfall();
            },
        });
    }else {
        console.log('传入的参数不正确！');
    }
}

//从后台获取分类列表，并显示
function getClassify(act) {
    if(act === 'index'){
        $.ajax({
            type: 'get',
            url: '/getclassify/',
            success: function (data) {
                html = '<option value="">请选择</option>';
                $.each(JSON.parse(data), function (index, content) {
                    html += ' <option value="' + content.id + '">' +
                        content.type_name + '</option>';
                });
                $('.classify-code').html(html);
            },
        });
    }else if(act === 'addurl') {
        $.ajax({
            type: 'get',
            url: '/getclassify/',
            success: function (data) {
                html = '<option value="">请选择</option>';
                $.each(JSON.parse(data), function (index, content) {
                    html += ' <option value="' + content.id + '">' +
                        content.type_name + '</option>';
                });
                $('.url-type').html(html);
            },
        });
    }else{
        console.log('传入的参数不正确！');
    }
}


//增加rul，并刷新页面数据展示最新的数据
function addUrl() {
    $.ajax({
        type: 'post',
        url: '/addurl/',
        data: $('.add-from').serialize(),
        success: function (data) {
            html = '';
            $.each(JSON.parse(data), function (index, content) {
                alert(content.messages);
            });
            $('#addurl').modal('hide');
            getUrls('get');
        },
    });
}


//增加分类，并刷新页面数据展示最新的数据
function addClassify() {
    $.ajax({
        type: 'post',
        url: '/addclassify/',
        data: $('.add-from').serialize(),
        success: function (data) {
            $.each(JSON.parse(data), function (index, content) {
                alert(content.messages);
            });
            $('#addclassify').modal('hide');
            getClassify('index');
            getClassify('addurl');
            getUrls('get');
        },
    });
}


//删除url
$('body').on("click", '.delete', function () {
    var url_name = $(this).parents("div.panel-footer").prevAll("div.panel-body").children("a.urls_link").text();
    var url_link = $(this).parents("div.panel-footer").prevAll("div.panel-body").children("a.urls_link").attr("href");
    $.ajax({
        type: 'post',
        url: '/delurl/',
        data: {"url_name": url_name, "url_link": url_link},
        success: function (data) {
            $.each(JSON.parse(data), function (index, content) {
                alert(content.retmsg);
                getUrls('get');
            })
        }
    })

})
function del_url() {
    console.log($(this));
    $.ajax({
        type: 'post',
        url: '/delurl/',
        data: $(this),
        success: function (data) {
            $.each(JSON.parse(data), function (index, content) {
                
            })
        }
    });
}


//删除分类
function del_classify() {
    $.ajax({
        type: 'post',
        url: '/delclassify/',
    });
}


//瀑布流布局
function waterfall() {
    $('.row').masonry({
        itemSelector: '.urls',
    });
};

function test(sss) {
    console.log(sss);
}
