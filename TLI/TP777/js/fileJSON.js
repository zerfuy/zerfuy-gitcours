function checkjson(data) {
  var isOk = true;
  try {
      var graphJSON = JSON.parse(data);
      try {
        var graph = graphJSON.graph;
        var graphName = graphJSON.graph.name;
        var graphDirected = graphJSON.graph.directed;
        //Verifie si la valeur est bien true or false
        if (!(graphDirected == true || graphDirected == false)) {
          isOk = false;
        }
        var graphVertices = graphJSON.graph.vertices;
        var graphEdges = graphJSON.graph.edges;

        //Verifie si les arretes pointe sur des sommets existants
        for(var i = 0; i < graphEdges.length; i++){
          var vertice1 = getVerticeById(graphEdges[i].id1, graphVertices);
          var vertice2 = getVerticeById(graphEdges[i].id2, graphVertices);
          if(vertice1 == -1 || vertice2 == -1){
            isOk = false;
          }
        }
      } catch(e) {
        isOk = false;
        alert("Le json ne possède pas tous les éléments pour récréer le graphe.")
      }
  } catch(e) {
    isOk = false;
    alert("Le fichier est un fichier json mais ne peut pas être parcouru. Vérifiez votre fichier.")
  }
  return isOk;
}

function openFile (event) {
  var input = event.target;
  var reader = new FileReader();
  reader.onload = function(){
    var dataURL = reader.result;
    console.log(dataURL);

    if (checkjson(dataURL)) {
      reinitialisationGraph(G);
      var graphJSON = JSON.parse(dataURL);

      G.directed = graphJSON.graph.directed;

      var tempVerticeCount = 0;
      for(var i = 0; i < graphJSON.graph.vertices.length; i++){
        if(graphJSON.graph.vertices[i].id > tempVerticeCount){
          tempVerticeCount = graphJSON.graph.vertices[i].id;
        }
      }
      console.log("verticeID : " + tempVerticeCount)
      G.verticeCount = tempVerticeCount+1;
      G.vertices = graphJSON.graph.vertices;
      G.edges = graphJSON.graph.edges;
      lastClickedVerticeId = -1;
      draggedVerticleId = -1;

      restartChoiceAlgo(G);
      updatePlan(G);
    } else {
      alert("Les données ne correspondent pas aux données attendues");
    }
  };

  if(input.files[0].type != "application/json") {
    alert("Le format de votre fichier n'est pas bon.");
  } else {
    reader.readAsText(input.files[0]);
  }
};

function exportJSON(graph) {
  var newLabel = prompt("Title of graph", "graph");
  
  var vertices = graph.vertices;
  var edges = graph.edges;
  var directedValue = graph.directed;

  var json =
  {
    graph : {
      name : newLabel,
      directed : directedValue,
      vertices,
      edges
    }
  }

  var jsonText = JSON.stringify(json)
  var blob = new Blob([jsonText], {type: "text/plain;charset=utf-8"});
  saveAs(blob, newLabel + ".json");
}

function exportJSONBipartite(classeA, classeB) {

  var classe_A = [];
  var classe_B = [];

  var elem;
  var temp;

  for (var i = 0; i < classeA.length; i++) {
    temp = classeA[i];
    elem = {
      id: temp,
    }
    classe_A.push(elem);
  }

  for (var i = 0; i < classeB.length; i++) {
    temp = classeB[i];
    elem = {
      id: temp,
    }
    classe_B.push(elem);
  }

  var json =
  {
    algorithm : {
      name : "biparti",
      classe_A : classe_A,
      classe_B : classe_B,
    }
  }

  var jsonText = JSON.stringify(json)
  var blob = new Blob([jsonText], {type: "text/plain;charset=utf-8"});
  saveAs(blob, "graphBiparti.json");
}

function exportJSONPageRank() {

}

function exportJSONDijkstra () {
  
}