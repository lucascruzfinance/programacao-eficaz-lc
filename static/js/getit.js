// Get-it — pequenas interações da página

// Pede confirmação antes de apagar uma anotação.
document.addEventListener("DOMContentLoaded", function () {
  const botoesApagar = document.querySelectorAll("[name='delete_button']");

  botoesApagar.forEach(function (botao) {
    botao.addEventListener("click", function (evento) {
      const confirmou = window.confirm("Tem certeza que deseja apagar esta anotação?");
      if (!confirmou) {
        evento.preventDefault();
      }
    });
  });
});
