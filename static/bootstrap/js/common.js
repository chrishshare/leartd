$(document).ajaxStart(function () {
    $('.loading-tfoot').show();
    $('.loading').show();
}).ajaxStop(function () {
    $('.loading').hide();
    $('.loading-tfoot').hide();
})