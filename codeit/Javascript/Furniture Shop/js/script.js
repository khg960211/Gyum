$('#popup-trigger').on('click', getCuppon);
$('#close-btn').on('click', closePopup);
$(document).on('keydown', closePopup);

function getCuppon() {
  $('#popup').fadeIn(1000);
}

function closePopup(event) {
  if (event.type == 'click') {
    $('#popup').fadeOut(1000);
  }
  else if (event.type == 'keydown') {
    if (event.key == 'Escape') {
      $('#popup').fadeOut(1000);
    }
  }
}
