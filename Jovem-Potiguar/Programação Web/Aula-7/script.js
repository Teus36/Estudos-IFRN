
function comentar() {
    const comentario = document.getElementById('comentario')
    const valor_comentario = comentario.value

    if (valor_comentario == '') {
        return 
    }

    document.getElementById('resultado').innerHTML += `<p>${valor_comentario}<button class="bg-red-500 text-white w-10 h-8 rounded-lg ml-2 transition ease-linear duration-250 hover:scale-110" onclick="deletar(this.parentElement)"> X </button></p><br>`
    comentario.value = ''

}

function deletar(elemento) {
    elemento.style.display = 'none'
}