var espec = parseFloat(prompt("Digite um número:"));
const num19 = 19

const diferença_abs = espec - num19

if (espec > 19){
    var triplo = diferença_abs * 3
    document.write(`Triplo da diferença absoluta entre ${espec} e ${num19}: ${triplo}`);
} else {
    document.write(`Diferença absoluta: ${diferença_abs}`);
}


