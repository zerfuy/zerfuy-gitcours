document.addEventListener('DOMContentLoaded', init);

function init(){

  var lienLogin = document.getElementById('linkLOGIN');
  if(localStorage.getItem('userName')){
    lienLogin.innerHTML = localStorage.getItem('userName');
  }

  var url = new URL(window.location);
  var params = new URLSearchParams(url.search);
  
  champs = [["lastname", params.get("lastname")],
   ["firstname", params.get("firstname")], 
   ["emailadress", params.get("emailadress")], 
   ["telephonenumber", params.get("telephonenumber")],
   ["startdate", params.get("startdate")], 
   ["returndate", params.get("returndate")], 
   ["numberadult", params.get("numberadult")], 
   ["numberkids", params.get("numberkids")], 
   ["infos", params.get("infos")],
   ["destination", params.get("destination")],
   ["totalprice", params.get("totalprice")]];

  for (i = 0; i < champs.length; i++) {
    document.getElementById(champs[i][0]).innerHTML = champs[i][1];
  }
}

function suppr(){
  var url = new URL(window.location);
  var params = new URLSearchParams(url.search);
  
  var i = params.get("indice");
  var tab = JSON.parse(localStorage.getItem("basket"));
  tab.splice(i, 1);
  localStorage.setItem("basket", JSON.stringify(tab));window.location.replace("index.html");
}