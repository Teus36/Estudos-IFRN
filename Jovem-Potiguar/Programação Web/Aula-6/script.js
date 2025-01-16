
function exibirUsers() {
    let inputi = document.getElementById("inputi").value;
    document.getElementById("resultado").innerHTML += `- ${inputi}<br>`
}


function exibirLista() {
    const lista = [1, 2, 3, 4, 5]
    document.getElementById("resultado2").innerHTML = `${lista}`
}

const lista = [1, 2, 5, 110]
let multi = 1 

for (var i = 0; i < lista.length; i++) {
    multi = multi * lista[i];
}

console.log(multi)