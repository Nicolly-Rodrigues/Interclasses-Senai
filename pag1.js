
  document.getElementById("btnCadastro").addEventListener("click", function() {
    window.location.href = "/usuario.html";
  });
// JavaScript para trocar fundo conforme scroll
const secoes = document.querySelectorAll("section");
const corpo = document.body;

function trocarFundoComScroll() {
  secoes.forEach(secao => {
    const retangulo = secao.getBoundingClientRect();
    const meioDaTela = window.innerHeight / 2;

    if (retangulo.top <= meioDaTela && retangulo.bottom >= meioDaTela) {
      const novaImagem = secao.getAttribute("data-bg");
      if (novaImagem) {
        corpo.style.backgroundImage = `url('${novaImagem}')`;
        corpo.style.backgroundSize = "cover";
        corpo.style.backgroundPosition = "center";
        corpo.style.backgroundRepeat = "no-repeat";
        corpo.style.transition = "background-image 0.8s ease-in-out";
      }
    }
  });
}

window.addEventListener("scroll", trocarFundoComScroll);
window.addEventListener("load", trocarFundoComScroll);
