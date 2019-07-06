// 배열
var members =['egoing', 'k8805', 'hoya'];
console.log(members[1]); //k8805
var i = 0;
while(i < members.length){
  console.log('array loop', members[i]);
  i += 1;
}

// 객체
var roles = {
  'programmer':'egoing', // key: value
  'designer':'k8805',
  'manager':'hoya'
};
console.log(roles.designer); // k8805
console.log(roles['designer']);

for(var name in roles){
  console.log('object => ', name, 'value => ', roles[name]);
}
