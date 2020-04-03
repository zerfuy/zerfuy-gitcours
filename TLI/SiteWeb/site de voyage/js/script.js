// Séjours et destinations
var Londres = {
  name: "Londres",
  price: 10,
  children: true,
  breakfast: true,
  img: "./images/londres.jpg",
}

var Melbourne = {
  name: "Melbourne",
  price: 20,
  children: true,
  breakfast: false,
  img: "./images/melbourne.jpg",
}

var Barcelona = {
  name: "Barcelona",
  price: 30,
  children: true,
  breakfast: true,
  img: "./images/barcelona.jpg",
}

var Fridge = {
  name: "Fridge",
  price: 40,
  children: false,
  breakfast: true,
  img: "./images/fridge.jpg",
}

destinations = [Londres, Melbourne, Barcelona, Fridge]
sorting_points = ["children", "breakfast"]

window.addEventListener("DOMContentLoaded", init)

//Fonction d'initialisation de la page d'accueil
function init(){
  if(!localStorage.getItem("basket")){
    localStorage.setItem('basket', JSON.stringify([]));
  }

  var lienLogin = document.getElementById('linkLOGIN');
  if(localStorage.getItem('userName')){
    lienLogin.innerHTML = localStorage.getItem('userName');
  }

  loadDestinations(true);
}  

function loadDestinations(firstInit){
  document.getElementById("mainContainer").innerHTML = "";

  if(!firstInit){
    for (i = 0; i < destinations.length; i++) {
      if (filteredIn(destinations[i])){
        gallery = document.createElement('div');
        gallery.className = 'gallery';
        a = document.createElement('a');
        if(localStorage.getItem('userName')){
          a.href = "./reservation.html?destination=".concat(destinations[i].name).concat("&price=").concat(destinations[i].price).concat("&img=").concat(destinations[i].img)
        }else{
          a.href = "./login.html";
        }
        img = document.createElement('img');
        img.src = destinations[i].img;
        img.alt = destinations[i].img;
        img.width = "600";
        img.height = "400";
        a.appendChild(img);
        desc = document.createElement('div');
        desc.className = "desc"
        desc.innerHTML = (destinations[i].name).concat(", ").concat((destinations[i].price)).concat("e par adulte");
        gallery.appendChild(a);
        gallery.appendChild(desc);
        document.getElementById('mainContainer').appendChild(gallery);
      }
    }
  }else{
    for (i = 0; i < destinations.length; i++) {
      gallery = document.createElement('div');
      gallery.className = 'gallery';
      a = document.createElement('a');
      if(localStorage.getItem('userName')){
        a.href = "./reservation.html?destination=".concat(destinations[i].name).concat("&price=").concat(destinations[i].price).concat("&img=").concat(destinations[i].img);
      }else{
        a.href = "./login.html";
      }
      img = document.createElement('img');
      img.src = destinations[i].img;
      img.alt = destinations[i].img;
      img.width = "600";
      img.height = "400";
      a.appendChild(img);
      desc = document.createElement('div');
      desc.className = "desc"
      desc.innerHTML = (destinations[i].name).concat(", ").concat((destinations[i].price)).concat("e par adulte");
      gallery.appendChild(a);
      gallery.appendChild(desc);
      document.getElementById('mainContainer').appendChild(gallery);
    }
  }
  
}

function filteredIn(destination){
  if (document.getElementById("childrenCheckbox").checked){
    if (!destination.children){
      return false;
    }
  }

  if (document.getElementById("breakfastCheckbox").checked){
    if (!destination.breakfast){
      return false;
    }
  }

  if (document.getElementById("MinPrice").value != ""){
    if (!(document.getElementById("MinPrice").value <= destination.price)){
      return false;
    }
  }

/*
  if (document.getElementById("MaxPrice").value != ""){
    if (!(destination.price <= document.getElementById("MaxPrice").value)){
      return false;
    }
  }

  if (document.getElementById("MaxDate").value != ""){
    if (!(destination.price <= document.getElementById("MinDate").value)){
      return false;
    }
  }

*/

  return true;
}