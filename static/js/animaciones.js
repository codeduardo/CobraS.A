window.addEventListener("scroll", function () {
  let animacion = document.getElementById("animado");
  let posicionObj1 = animacion.getBoundingClientRect().top;
  console.log(posicionObj1);
});
