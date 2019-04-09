$('button').on('click', function (event) {
  if (event.currentTarget.id == 'even-btn') {
    $('.card').each(function () {
      $(this).removeClass("selected");
      var value = $(this).text();
      if (value % 2 == '0') {
        $(this).addClass("selected");
      }
    });
  }
  else if (event.currentTarget.id == 'odd-btn'){
    $('.card').each(function () {
      $(this).removeClass("selected");
      var value = $(this).text();
      if (value % 2 != '0') {
        $(this).addClass("selected");
      }
    });
  }
});
