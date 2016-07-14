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
        $('.lightbox.close-button').removeClass('hidden');
    });

    $('.lightbox.close-button .close-button').click(function (){
        event.preventDefault();
       $('.lightbox.close-button').addClass('hidden'); 
    });



});