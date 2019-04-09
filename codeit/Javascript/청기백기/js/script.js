$('#btn1').on('click', downBF);
$('#btn2').on('click', downWF);
$('#btn3').on('click', downDotBF);

function downBF() {
$('img:nth-child(3)').addClass("down");
$('img:nth-child(6)').addClass("down");
setTimeout(upFlag, 1000);
}

function downWF() {
$('.white').addClass("down");
setTimeout(upFlag, 1000);
}

function downDotBF() {
$('.blue.dot').addClass("down");
setTimeout(upFlag, 1000);
}

function upFlag() {
  $('img').removeClass("down");
}
