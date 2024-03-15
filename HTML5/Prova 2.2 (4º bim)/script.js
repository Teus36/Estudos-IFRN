document.getElementById("trocar_cor").addEventListener("click", function () {
    let cor = document.getElementById("cor");
    let caixa = document.querySelector("#caixa");

    if (cor = "blue") {
        caixa.style.backgroundColor = "blue";
        caixa.style.color = "white"
    }
})

document.getElementById("trocar_conteudo").addEventListener("click", function () {
    let num = document.getElementById("num");
    let caixa = document.getElementById("caixa");

    if (num = 1) {
        caixa.textContent = "Mateus Batista Almeida";
    }
})