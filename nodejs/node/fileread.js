var fs = require('fs');
fs.readFile('node/sample.txt', 'utf-8', function(err, data){
  console.log(data);
});
