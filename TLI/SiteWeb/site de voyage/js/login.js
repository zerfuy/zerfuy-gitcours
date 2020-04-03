// Séjours et destinations
var user1 = {
  username: "user1",
  password: "mdp1",
}

var user2 = {
  username: "user2",
  password: "mdp2",
}

var user3 = {
  username: "user3",
  password: "mdp3",
}

var user4 = {
  username: "user4",
  password: "mdp4",
}

users = [user1, user2, user3, user4]

window.addEventListener("DOMContentLoaded", init);

function init () {
  var login = document.getElementById('formLogin');
  var logout = document.getElementById('formLogout');
  var lienLogin = document.getElementById('linkLOGIN');
  if(localStorage.getItem('userName')){
    lienLogin.innerHTML = localStorage.getItem('userName');
    login.innerHTML = "";
  }  else {
    logout.innerHTML = "";
  }
}

function logout(){
  localStorage.clear();
}

function submitForm() {
  var login = document.getElementById('login');
  var mdp = document.getElementById('mdp');
  var auth = false;

  for (i = 0; i < users.length; i++) {
    if(users[i].username == login.value && users[i].password == mdp.value){
      auth = true;
      var stock = window.localStorage;
      stock.setItem('userName', users[i].username);
    }
  }

  if (auth) {
    alert('Authentification réussi !');
  } else {
    alert('Erreur lors de l authentification !');
  }
}