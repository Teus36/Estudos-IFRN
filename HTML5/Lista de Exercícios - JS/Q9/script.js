var num1 = parseFloat(prompt("Digite o primeiro número:"));
var num2 = parseFloat(prompt("Digite o segundo número:"));

if (num1 > 0 && num2 < 0 || num1 < 0 && num2 > 0)
    document.write("Temos um valor positivo e outro negativo")
else {
    document.write("Os dois valores possuem o mesmo sinal")
}