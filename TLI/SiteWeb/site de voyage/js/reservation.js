//Ajoute les événements sur les éléments du formulaire pour faire les vérifications et des update necessaire
document.addEventListener('DOMContentLoaded', function(){

  var lienLogin = document.getElementById('linkLOGIN');
  if(localStorage.getItem('userName')){
    lienLogin.innerHTML = localStorage.getItem('userName');
  }

  var url = new URL(window.location);
  var params = new URLSearchParams(url.search);

  document.getElementById('destination').value=params.get("destination");
  document.getElementById('destination').readOnly = true;
  document.getElementById('price').innerHTML=params.get("price");
  document.getElementById('img').value=params.get("img");
  
  document.getElementById("submitbtn").disabled = true;

  document.getElementById('lastname').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
  }, false);

  document.getElementById('firstname').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
  }, false);

  document.getElementById('emailadress').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
  }, false);

  document.getElementById('startdate').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
    updateTotalPrice();
  }, false);

  document.getElementById('returndate').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
    updateTotalPrice();
  }, false);

  document.getElementById('numberadult').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
    updateTotalPrice();
  }, false);

  document.getElementById('breakfast').addEventListener( 'click', function() {
    updateTotalPrice();
  }, false);

  document.getElementById('numberkids').addEventListener( 'focusout', function() {
    changeStateSubmitButton(checkValideForm());
    updateTotalPrice();
  }, false);
}, false);

//Verifie si le formulaire est ok pour etre submmit
function checkValideForm() {
  var nom = document.getElementById('lastname');
  var prenom = document.getElementById('firstname');
  var adMail = document.getElementById('emailadress');
  var dateDepart = document.getElementById('startdate');
  var dateRetour = document.getElementById('returndate');
  var nbAdultes = document.getElementById('numberadult');
  var nbEnfants = document.getElementById('numberkids');
  var validation = true;

  if(nom.value == '') {
    validation = false;
  } else if (prenom.value == '') {
    validation = false;
  } else if (adMail.value == '' || !adMail.validity.valid) {
    validation = false;
  }  else if (dateDepart.value == '') {
    validation = false;
  } else if (dateRetour.value == '' || dateRetour.value < dateDepart.value) {
    validation = false;
  } else if (nbAdultes.value == '' || nbAdultes.value > 99 || nbAdultes.value < 1) {
    validation = false;
  } else if (nbEnfants.value == '' || nbEnfants.value > 99  || nbEnfants.value < 0) {
    validation = false;
  }
  return validation;
}

//Active / désactive le bouton submit
function changeStateSubmitButton(validation){
  if(validation == true){
    document.getElementById("submitbtn").disabled = false;
  } else {
    document.getElementById("submitbtn").disabled = true;
  }
}

//Update le prix du séjour en fonction des options choisies
function updateTotalPrice() {
  var prixTotal = document.getElementById('totalprice');

  var destination = document.getElementById('destination');
  var dateDepart = document.getElementById('startdate');
  var dateRetour = document.getElementById('returndate');
  var nbAdultes = document.getElementById('numberadult');
  var nbEnfants = document.getElementById('numberkids');
  var petitDej = document.getElementById('breakfast');

  var prixCalcule = 0;
  var prixJour = document.getElementById('price').innerHTML
  var nbJour = 0;

  if (dateDepart.value != '' && dateRetour.value != '' && dateDepart.value < dateRetour.value) {
     nbJour = datediff(parseDate(dateDepart.value), parseDate(dateRetour.value))
  }

  if(nbAdultes.validity.valid && nbAdultes.value != ''){
    prixCalcule = prixCalcule + (prixJour * nbAdultes.value * nbJour);
  }
 
  if(nbEnfants.validity.valid && nbEnfants.value != ''){
    prixCalcule = prixCalcule + (prixJour * nbEnfants.value * 0.4 * nbJour);
  }

  if(petitDej.checked && nbAdultes.validity.valid && nbAdultes.value != ''){
	  prixCalcule = prixCalcule + (8*nbAdultes.value*nbJour);
  }

  if(petitDej.checked && nbEnfants.validity.valid && nbEnfants.value != ''){
	  prixCalcule = prixCalcule + (8*nbEnfants.value*nbJour);
  }

  prixTotal.value = prixCalcule;
}

//reset tous les champs du formulaire
function resetForm() {
  document.getElementById("formReservation").reset();
  document.getElementById("submitbtn").disabled = true;
}

//Fonctions pour les dates
function parseDate(str) {
    var mdy = str.split('-');
    return new Date(mdy[2], mdy[0]-1, mdy[1]);
}

function datediff(first, second) {
    // Take the difference between the dates and divide by milliseconds per day.
    // Round to nearest whole number to deal with DST.
    return Math.round((second-first)/(1000*60*60*24*365));
}