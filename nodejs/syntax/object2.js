var f = function(){
  console.log(1+1);
  console.log(1+2);
}
// 배열의 원소로서 함수가 존재할 수 있다.
var a = [f];
a[0]();

var o = {
  func:f
}
o.func();
