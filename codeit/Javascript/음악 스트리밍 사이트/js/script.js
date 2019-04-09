// document는 전체 문서
// window는 현재 보이는 화면

$(window).on('scroll', scrollHandler);

function scrollHandler() {
  var windowBottom = $(window).height() + $(window).scrollTop();

  $('.playlist').each(function() {
    // offset().top은 문서 맨 위에서 해당 태그까지의 길이를 리턴
    // 그 값에 해당 태그 높이의 절반을 더하면 됨
    var playlistCenter = $(this).height() / 2 + $(this).offset().top;

    // 밑으로 갈 수록 좌표값이 커지므로
    if (windowBottom >= playlistCenter) {
      $(this).animate({opacity: "1"}, 1000);
    }

  });

  if ($(document).height() === windowBottom) {
    $('.to-top-btn').fadeIn(1000);
    $('.to-top-btn').on('click', function () {
      $('html').animate({scrollTop: 0}, 1000);
    })
  }
  else {
    $('.to-top-btn').fadeOut(1000);
  }
}
// scrollHandler 함수는 스크롤을 해야만 실행된다.
// 즉, 페이지 로딩 직후에도 약간의 스크롤을 해주어야만 playlist가 나온다.
// 이럴 경우 scroll 이벤트에 연결된 코드를 js 파일 내에 한 번 실행해주면 해결된다.
// 그것이 아래의 코드이다.
scrollHandler();
