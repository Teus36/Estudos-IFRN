var num1 = parseFloat(prompt("Digite o primeiro número:"));
var num2 = parseFloat(prompt("Digite o segundo número:"));

var soma = num1 + num2;

if (num1 == num2) {
    var triplo = soma * 3
    document.write("Triplo da soma entre o primeiro e segundo número: " + triplo);
} else {
    document.write("Soma entre o primeiro e segundo número: " + soma);
}

