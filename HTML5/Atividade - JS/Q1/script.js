const botao = document.createElement('button');
botao.textContent = 'Clique aqui';
botao.id = 'meuBotao';

document.body.appendChild(botao);

botao.addEventListener('click', function() {
    console.log('Botão clicado!');
});