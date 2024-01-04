document.getElementById("calcular").addEventListener("click", function () {
    
    var num = parseInt(document.querySelector("#num input").value);
    var inicio = parseInt(document.querySelector("#inicio input").value);
    var fim = parseInt(document.querySelector("#fim input").value);
    var tabela = document.getElementById("tabela");
    tabela.border = '1px'
    document.getElementById("tabela").innerHTML = "";

    // Cria a primeira linha da tabela com os títulos
    var cabecalho = tabela.createTHead();
    var linhaTitulo = cabecalho.insertRow(0);
    var celulaTitulo = linhaTitulo.insertCell(0);
    celulaTitulo.innerHTML = "<strong>Tabuada do " + num + " de " + inicio + " a " + fim + "</strong>";

    // Cria as linhas e colunas da tabela
    for (var i = inicio; i <= fim; i++) {
        var linha = tabela.insertRow(i - inicio + 1);
        var coluna1 = linha.insertCell(0);
        var coluna2 = linha.insertCell(1);

        coluna1.innerHTML = "<strong>" + num + " x " + i + "</strong>";
        coluna2.innerHTML = num * i;
    }
});