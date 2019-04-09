var audioFile = []
audioFile.push(new Audio('audio/audio/loop.mp3'));
audioFile.push(new Audio('audio/audio/01_kick_drum.wav'));
audioFile.push(new Audio('audio/audio/02_closed_hihat.wav'));
audioFile.push(new Audio('audio/audio/03_open_hihat.wav'));
audioFile.push(new Audio('audio/audio/04_clap.wav'));
audioFile.push(new Audio('audio/audio/05_snap.wav'));
audioFile.push(new Audio('audio/audio/06_crash.wav'));
audioFile.push(new Audio('audio/audio/07_tom1.wav'));
audioFile.push(new Audio('audio/audio/08_tom2.wav'));
audioFile.push(new Audio('audio/audio/09_tambourine.wav'));

$('#play-btn').on('click', playMusic);
$('#stop-btn').on('click', stopMusic);
$(document).on('keydown', keyDownEvent);
$(document).on('keyup', keyUpEvent);

function playMusic() {
  audioFile[0].play();
}
function stopMusic() {
  audioFile[0].pause();
  audioFile[0].currentTime = 0;
}
function keyDownEvent(event) {
  if (event['key'] >= 1 && event['key'] <= 9) {
    $('#cell' + event['key']).addClass("playing");
    audioFile[Number(event['key'])].play();
    audioFile[Number(event['key'])].currentTime = 0;
  }
}
function keyUpEvent(event) {
  $('.cell').removeClass("playing");
}
