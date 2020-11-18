$(function () {
    var shrinkHeader = 300;
    $(window).scroll(function () {
        var scroll = getCurrentScroll();
        if (scroll >= shrinkHeader) {
            $('.header').addClass('shrink');
        } else {
            $('.header').removeClass('shrink');
        }
    });

    function getCurrentScroll() {
        return window.pageYOffset || document.documentElement.scrollTop;
    }
});
