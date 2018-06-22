(function($) {
    $(document).ready(function() {
        $('.tabs-title .login').on('click', function() {
            $(this).parent('.tabs-title').parent('.container').addClass('login_container');
            $('.tabs-title .register').removeClass('active');
            $(this).addClass('active');
            $('.tabs-content .login').show();
            $('.tabs-content .registration').hide();
        });
        $('.tabs-title .register').on('click', function() {
            $(this).parent('.tabs-title').parent('.container').removeClass('login_container');
            $('.tabs-title .login').removeClass('active');
            $(this).addClass('active');
            $('.tabs-content .registration').show();
            $('.tabs-content .login').hide();
        });
        $('.row .fas').on('click', function() {
            $(this).parent().parent().toggleClass('active');
        });

        $('#header .cart-block > a').on('click', function(e){
            e.preventDefault();
        });

        $('#cart-info .cart-block').mouseover(function(){
            $('#cartview').addClass('block');
        });
        var timer;
        var delay = 1000;
        $('#cart-info .cart-block').mouseout(function() {
            timer = setTimeout(function() {
                $('#cartview').removeClass('block');
            }, delay);
        });

        $(window).on('load', function() {
            if ( $(window).width() < 768 ) {
                $('#header .checkout-block button > a').on('click', function(e){
                    e.preventDefault();
                });
                $('#user-block .dropdown > li').on('hover', function(e){
                    $('.dropdown-menu').addClass('none');
                });
            }
        });
        $(window).on('load', function() {
            if ( $(window).width() < 540 ) {
                $('#search-block').on('click', function(){
                    $('.header-bottom').addClass('search');
                    $('#header .hamburger').addClass('none');
                    $('#header .logo').addClass('none');
                    $('#cart-info .cart-block > a').addClass('none');
                    $('#search-block').addClass('width');
                    $('#search_cancel').addClass('open');
                });
                $('#search_cancel').on('click', function(){
                    $('.header-bottom').removeClass('search');
                    $('#header .hamburger').removeClass('none');
                    $('#header .logo').removeClass('none');
                    $('#cart-info .cart-block > a').removeClass('none');
                    $('#search-block').removeClass('width');
                    $('#search_cancel').removeClass('open');
                });
               //  $(document).on("vclick", "#search-block", function() {
               //     $('#header .hamburger').addClass('none');
               //     $('#header .logo').addClass('none');
               //     $('#cart-info').addClass('none');
               //     $('#search-block').addClass('width');
               // });
           }
       });
        $(window).on('load', function(){
            if ($('#cartview .item').height > 500){
                $('#cartview').addClass('scroll');
            }else{
                $('#cartview').removeClass('scroll');
            }
        });

        $('#brand_filter .color-item input').change(function (e) {
            e.preventDefault();
            if ($(this).is(':checked')){
                $(this).parent().addClass('checked')
            }else{
                $(this).parent().removeClass('checked')
            }
        });
        $('#brand_filter .brand_item input').change(function (e) {
            e.preventDefault();
            if ($(this).is(':checked')){
                $(this).parent().addClass('checked')
            }else{
                $(this).parent().removeClass('checked')
            }
        });
        $('#brand_filter .feature_item input').change(function (e) {
            e.preventDefault();
            if ($(this).is(':checked')){
                $(this).parent().addClass('checked')
            }else{
                $(this).parent().removeClass('checked')
            }
        });
        $('#cart-info').on('click', function(){
            $('#cartview').addClass('hover');
        });
        $("#cart-info").swipe({
            swipeRight: function() {
                $('#cartview').removeClass('hover');
            }
        });
        $('.mobile_filter_btn > button').on('click', function(){
            $('#filterview').html($('#brand_filter').parent().html());
            $('#brand_filter').empty();
            $('#filterview').addClass('hover');

        });
        $('#center').swipe({
            swipeRight: function() {
                $('#filterview').removeClass('hover');
                $('#brand_filter').html($('#filterview').parent().html());
                $('#filterview').empty();
            }
        });
    }); //doc ready end--------------------------------
}(jQuery));