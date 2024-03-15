//adicionar cards ao elementos

//criar uma âncora
let a = document.createElement('button');
a.innerText = 'Adicionar Card';
a.setAttribute('id', 'botao');

//adicionar ao li
let li = document.getElementById('li')
li.innerHTML = a.outerHTML;

//adicionar evento para adicionar cards
let botao = document.getElementById('li');
botao.addEventListener ('click', (event)=>{
    
   let content = document.getElementsByClassName('content')[0];
   let elem = document.createElement('div');
   elem.classList.add('card');
   content.append(elem);
}); 

//limpar o container

const limpar = document.getElementById('limpar')
limpar.addEventListener('click', (event)=>{
    const content = document.getElementsByClassName('content')[0];
    content.innerHTML = '';
});


