$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() !== 0) {
            $('#topButtom').fadeIn();
        } else {
            $('#topButtom').fadeOut();
        }
    });
    $('#topButtom').click(function () {
        $('body,html').animate({scrollTop: 0}, 700);
    });
});


$(document).ready(function () {

    $(".fa-search").click(function () {
        $(".container, .input").toggleClass("active");
        $("input[type='text']").focus();
    });

});


$(document).ready(function () {
    bsCustomFileInput.init()
})
