var num_dado = parseFloat(prompt("Digite o primeiro número:"));
const num400 = 400;
const num100 = 100;

const diferença_abs400 = 400 - num_dado
const diferença_abs100 = 100 - num_dado

if (diferença_abs400 <= 20 || diferença_abs100 <=20) {
    document.write("Está dentro do valor 20")
} else {
    document.write("Não está dentro do valor 20")
}