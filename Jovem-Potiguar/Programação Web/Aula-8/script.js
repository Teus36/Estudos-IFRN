let estados = []

fetch('https://servicodados.ibge.gov.br/api/v1/localidades/estados', {
    method: 'GET'
}).then(async (resposta) => {
    estados = (await resposta.json())
    const selectEstados = document.getElementById('estado')
    for (let i = 0; i < estados.length; i++) {
        selectEstados.innerHTML += `<option value="${estados[i].id}">${estados[i].nome}</option>`
    }
})

function exibirCidades(estado) {
    const selectCidades = document.getElementById('cidade')
    selectCidades.innerHTML = ""
    fetch(`https://servicodados.ibge.gov.br/api/v1/localidades/estados/${estado}/municipios`, {
    method: 'GET'    
}).then(async (resposta) => {
    const cidades = (await resposta.json())
    for (let i = 0; i < cidades.length; i++) {
        selectCidades.innerHTML += `<option value="${cidades[i].id}}">${cidades[i].nome}</option>`
    }
    })
}