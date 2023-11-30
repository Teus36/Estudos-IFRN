var num1 = parseFloat(prompt("Digite o primeiro número:"));
var num2 = parseFloat(prompt("Digite o segundo número:"));

if (num1 + num2 === 50 || num1 === 50 || num2 === 50) {
    var verify = true
    document.write(verify)
} else {
    var verify = false
    document.write(verify)
}