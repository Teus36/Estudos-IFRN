var x = 5;
var y = 6;
var z = 7;

var p = (x+y+z)/ 2;
var A = p*(p-x)*(p-y)*(p-z);
var raiz = Math.sqrt(A).toFixed(2);

console.log(raiz)