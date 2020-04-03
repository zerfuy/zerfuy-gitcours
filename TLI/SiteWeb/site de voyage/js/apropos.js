window.addEventListener("DOMContentLoaded", init);

function init(){
  var lienLogin = document.getElementById('linkLOGIN');
  if(localStorage.getItem('userName')){
    lienLogin.innerHTML = localStorage.getItem('userName');
  }
}