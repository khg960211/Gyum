$(window).on('scroll', scrollHandler);
// 참고 : $('.about').position().top; -> about 태그의 맨 윗부분 좌표

$('#about-btn').on('click', function () {
  $('html').animate({scrollTop: $('.header').height()}, 1000);
});
$('#contact-btn').on('click', function() {
  var moveContact = $('.header').height() + $('.about').height();
  $('html').animate({scrollTop: moveContact}, 1000);
});
// $('.menu-right button').on('click', function () {
//   var id = $(this).attr('id');
//   if (if == 'about-btn') {
//     $('html body').animate({scrollTop: $('.about').position().top}, 1000);
//   }
//   else if (id == 'contact-btn') {
//     $('html body').animate({scrollTop: $('.contact').position().top}, 1000);
//   }
// });

function scrollHandler() {
  var bottomHeader = $('.header').height();

  if ($(window).scrollTop() >= bottomHeader) {
    $('#about-btn').css('color', '#4a4a4a');
    $('#contact-btn').css('color', '#4a4a4a');
    $('.skill').each(function () {
      var width = $(this).find('.percentage').text();
      $(this).find('.inner-bar').animate({'width': width}, 1000);
    });
  }
  else {
    $('#about-btn').css('color', 'white');
    $('#contact-btn').css('color', 'white');
  }
  
  $('section').each(function () {
    if ($(window).scrollTop() >= $(this).position().top) {
      $(this).find('.vertical-center').animate({opacity: '1', top: '0px'}, 1000);
    }
  });
}
scrollHandler();
