$(function (){
    $('.open-lightbox-not-focused').click(function (event){
        event.preventDefault();
        $('.lightbox.not-focused').removeClass('hidden');
    });

    $('.lightbox.not-focused .close-button').click(function (){
        event.preventDefault();
       $('.lightbox.not-focused').addClass('hidden'); 
    });

    $('.open-lightbox-close-button').click(function (event){
        event.preventDefault();
        var $lClose = $('.lightbox.close-button');
        $lClose.removeClass('hidden');
        $lClose.focus();
    });

    $('.lightbox.close-button .close-button').click(function (){
        event.preventDefault();
       $('.lightbox.close-button').addClass('hidden'); 
    });

    $('.open-lightbox-focus-far').click(function (event){
        event.preventDefault();
        var $lbox = $('.lightbox.focus-far');
        $('body').append($lbox);
        $lbox.removeClass('hidden');
    });

    $('.lightbox.focus-far .close-button').click(function (){
        event.preventDefault();
       $('.lightbox.focus-far').addClass('hidden'); 
    });

    $('.open-lightbox-unescapable').click(function (event){
        event.preventDefault();
        $('.lightbox.unescapable').removeClass('hidden');
    });

    $('.lightbox.unescapable .close-button').click(function (){
        event.preventDefault();
       $('.lightbox.unescapable').addClass('hidden'); 
    });

    // escape key to close lightboxes
    $(window).keyup(function (e){
        if (e.keyCode == 27) { //escape key
            $('.lightbox').not('.unescapable').addClass('hidden');
        }
    });

    /* Concertina */

    $('.concertina dd').addClass('hidden');

    $('.concertina dt').click(function (e){
        var $dt = $(this);
        var $dd = $dt.next('dd');
        $dt.toggleClass('expanded');
        $dd.toggleClass('hidden');
    });

    $('.language-selector').change(function (){
        window.location = window.location.href;
    });

    $('.tooltip-icon')

});