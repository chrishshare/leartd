$(document).ajaxStart(function () {
    $('.loader').show();
}).ajaxStop(function () {
    $('.loader').hide();
})