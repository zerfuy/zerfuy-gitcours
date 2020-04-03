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
   ["totalprice", params.get("totalprice")],
   ["img", params.get("img")]];

  for (i = 0; i < champs.length; i++) {
    if(champs[i][1] != "img"){
      document.getElementById(champs[i][0]).innerHTML = champs[i][1];
    }
  }
}

function addToBasket(){
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
   ["totalprice", params.get("totalprice")],
   ["img", params.get("img")]];

  var destination = {
    lastname: champs[0][1],
    firstname: champs[1][1],
    emailadress: champs[2][1],
    telephonenumber: champs[3][1],
    startdate: champs[4][1],
    returndate: champs[5][1],
    numberadult: champs[6][1],
    numberkids: champs[7][1],
    infos: champs[8][1],
    destination: champs[9][1],
    totalprice: champs[10][1],
    img: champs[11][1]
  }
  var tab = JSON.parse(localStorage.getItem("basket"));
  tab.push(destination);
  localStorage.setItem("basket", JSON.stringify(tab));
  
}