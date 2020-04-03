document.addEventListener('DOMContentLoaded', init);

function init () {
	var url = "./cryptomonnaies/cryptomonnaies.json";
	var data = {};
	var donnees = {};
	var xmlhttp = new XMLHttpRequest();
	xmlhttp.open("GET", url, true);
	                                
	xmlhttp.onreadystatechange = function () {
	  	if (xmlhttp.readyState == 4 && xmlhttp.status == 200){
	    	data = JSON.parse(xmlhttp.responseText);
	    	donnees = data.data;
	    	console.log(donnees);

	    	donnees.sort(function(a, b) {
  				var nameA=a.name.toLowerCase(), nameB=b.name.toLowerCase()
			    if (nameA < nameB) //sort string ascending
			        return -1 
			    if (nameA > nameB)
			        return 1
			    return 0 //default return value (no sorting)
			});

			var select = document.getElementById("select");

			for(var i = 0; i < donnees.length; i++){
				var option = document.createElement("option");
				option.setAttribute("value", donnees[i].id);
				option.innerHTML = donnees[i].name;
				select.appendChild(option);
			}
			$("select").trigger("change");
	  	}
	};
	xmlhttp.send();

	$("select").change(function(event){

		var monnaie = {};
		for(var i = 0; i < donnees.length; i++){
			if(donnees[i].id == this.value){
				monnaie = donnees[i];
			}
		}

		var infos = document.getElementById("infosMonnaie");
		infos.innerHTML = "";

		var noms = document.createElement("p");
		noms.innerHTML = monnaie.name;

		var symbole = document.createElement("p");
		symbole.innerHTML = monnaie.symbol;

		var cours = document.createElement("p");
		cours.innerHTML = monnaie.quote.EUR.price;

		infos.appendChild(noms);
		infos.appendChild(symbole);
		infos.appendChild(cours);
	});
}



