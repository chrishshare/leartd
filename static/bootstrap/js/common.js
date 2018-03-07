$(document).ajaxStart(function () {
    $('.loading-tfoot').show();
    $('.loading').show();
    $('.loader').show();
}).ajaxStop(function () {
    $('.loading').hide();
    $('.loading-tfoot').hide();
    $('.loader').hide();
})