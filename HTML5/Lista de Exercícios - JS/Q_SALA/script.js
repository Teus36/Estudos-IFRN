function mostrarHora() {
    const span = document.getElementById('clock');
    let now = new Data();
    span.InnerText = now.toLocaleTimeString();
}

mostrarHora();

setInterval(mostrarHora, 1000);