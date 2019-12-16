$(function () {
    initTopSwiper();
    initSwiperMenu();
})

function initTopSwiper() {
    var swiper = new Swiper("#topSwiper",{
        loop:true,
        autoplay:2000,
        pagination: '.swiper-pagination'
    });
}

function initSwiperMenu() {
    var swiper = new Swiper("#swiperHot",{
        slidesPerView:3,
    });
}