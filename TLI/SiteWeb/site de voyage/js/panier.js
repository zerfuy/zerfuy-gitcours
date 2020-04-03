window.addEventListener("DOMContentLoaded", init)

//Fonction d'initialisation de la page d'accueil
function init(){
  if(!localStorage.getItem('userName')){
    document.location.href="login.html";
  }

  var lienLogin = document.getElementById('linkLOGIN');
  if(localStorage.getItem('userName')){
    lienLogin.innerHTML = localStorage.getItem('userName');
  }
  
  loadReservations();

} 

function loadReservations(){
  var contentPanier = document.getElementById('contentPanier');
  var destinations = JSON.parse(localStorage.getItem("basket"));

  console.log(destinations)

  if (destinations.length == 0) {
    contentPanier.innerHTML = '<p> Votre panier est vide !</p> <input type="button" onclick="redirectAccueil();" value ="Ajouter des voyages">';
  } else {
    for (i = 0; i < destinations.length; i++) {
      gallery = document.createElement('div');
      gallery.className = 'gallery';
	  linkImage = document.createElement('a');
	  linkImage.setAttribute("href", "destSummary.html?".concat("&lastname=").concat(destinations[i].lastname).concat("&firstname=").concat(destinations[i].firstname).concat("&emailadress=").concat(destinations[i].emailadress).concat("&telephonenumber=").concat(destinations[i].telephonenumber).concat("&startdate=").concat(destinations[i].startdate).concat("&returndate=").concat(destinations[i].returndate).concat("&numberadult=").concat(destinations[i].numberadult).concat("&numberkids=").concat(destinations[i].numberkids).concat("&infos=").concat(destinations[i].infos).concat("&destination=").concat(destinations[i].destination).concat("&totalprice=").concat(destinations[i].totalprice).concat("&indice=").concat(i));
      image = document.createElement('img');
      image.setAttribute("src", destinations[i].img);
      image.setAttribute("alt", "destinationPicture");
	  linkImage.appendChild(image);
      desc = document.createElement('a');
      desc.innerHTML = destinations[i].destination  +": Du "+destinations[i].startdate +" au " + destinations[i].returndate + ", pour un total de " + destinations[i].totalprice +" euros.";
      desc.setAttribute("href", "destSummary.html?".concat("&lastname=").concat(destinations[i].lastname).concat("&firstname=").concat(destinations[i].firstname).concat("&emailadress=").concat(destinations[i].emailadress).concat("&telephonenumber=").concat(destinations[i].telephonenumber).concat("&startdate=").concat(destinations[i].startdate).concat("&returndate=").concat(destinations[i].returndate).concat("&numberadult=").concat(destinations[i].numberadult).concat("&numberkids=").concat(destinations[i].numberkids).concat("&infos=").concat(destinations[i].infos).concat("&destination=").concat(destinations[i].destination).concat("&totalprice=").concat(destinations[i].totalprice).concat("&indice=").concat(i));
      
	  gallery.appendChild(linkImage);
      gallery.appendChild(desc);
      contentPanier.appendChild(gallery);
    }
  }
}

function redirectAccueil(){
  document.location.href="index.html";
}