var chat ={
	saisie: document.getElementById("zoneSaisie"),
	posterMessage: function() {
		var xmlhttp = new XMLHttpRequest();
    	var url = new URL(window.location);
    	var params = new URLSearchParams(url.search);
    	var user = params.get("user");
    	console.log(user + "posted");
    	var msg = document.getElementById("zoneSaisie").value;

    	var params = new FormData();
    	params.append("method", "poster");
    	params.append("user_id", user);
    	params.append("message", msg);

		xmlhttp.onreadystatechange = function () {
		  	if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
		    	
		  	}
		};
		xmlhttp.open("POST", "ajax/chat.php", true);   
		xmlhttp.send(params);  
  	},
  	recupererMessages: function() {  
  		var xmlhttp = new XMLHttpRequest();
    	var url = new URL(window.location);
    	var params = new URLSearchParams(url.search);

    	var user = params.get("user");
    	console.log(user + "received");
    	var params = new FormData();
    	params.append("method", "recuperer");
       
		xmlhttp.onreadystatechange = function () {
		  	if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
		    	document.getElementById("messages").innerHTML = xmlhttp.responseText;
		  	}
		};
		xmlhttp.open("POST", "ajax/chat.php", true);
		xmlhttp.send(params);
  	}
}

document.addEventListener('DOMContentLoaded', init);

function init () {
	$("#zoneSaisie").on("keydown", function envoyer(e){
		if(e.keyCode == 13) {
			if (!event.shiftKey){
				event.preventDefault();
				chat.posterMessage();
				document.getElementById("zoneSaisie").value = "";	
			}
		}
	});

	setInterval(function(){
		chat.recupererMessages();
	}, 2000);
}