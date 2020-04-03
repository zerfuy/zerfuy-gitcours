function isBipartite (graph) {

  var vertices = graph.vertices;
  var edges = graph.edges;
  var classeA = [];
  var classeB = [];

  var biparti = true;

  // Boucles sur chaque sommet
  for(var i = 0; i < vertices.length; i++){

    arrayPointedVerticesIds = getPointedVerticesIds(vertices[i], edges);
    arrayVerticesPointingCurrentVertice = getPointingToVertices(vertices[i], edges);

    if(classeA.includes(vertices[i].id)) {

      if(containsVertice(classeA , arrayPointedVerticesIds)) {
        biparti = false; break;
      } else if (containsVertice(classeA , arrayVerticesPointingCurrentVertice)){
        biparti = false; break;
      } else {
        addVerticesIdsToClass(classeB, arrayPointedVerticesIds);
        addVerticesIdsToClass(classeB, arrayVerticesPointingCurrentVertice);
      }

    } else if (classeB.includes(vertices[i].id)) {

      if(containsVertice(classeB , arrayPointedVerticesIds)) {
        biparti = false; break;
      } else if (containsVertice(classeB , arrayVerticesPointingCurrentVertice)){
        biparti = false; break;
      } else {
        addVerticesIdsToClass(classeA, arrayPointedVerticesIds);
        addVerticesIdsToClass(classeA, arrayVerticesPointingCurrentVertice);
      }

    } else {
      //On l'ajoute dans la classeA
      classeA.push(vertices[i].id);
      //On vérifie que les sommets sur lesquels ils pointent ne sont pas dans la meme classe
      if(containsVertice(classeA , arrayPointedVerticesIds)) {
        biparti = false; break;
      } else if (containsVertice(classeA , arrayVerticesPointingCurrentVertice)){
        biparti = false; break;
      } else {
        addVerticesIdsToClass(classeB, arrayPointedVerticesIds);
        addVerticesIdsToClass(classeB, arrayVerticesPointingCurrentVertice);
      }
    }
  }

  if (biparti) {
    alert("Votre graphe est biparti !");
    colorGraph(classeA, classeB, vertices);
    exportJSONBipartite(classeA, classeB);
  } else {
    alert("Votre graphe n'est pas biparti !");
  }
}


//----------------------------------------------------------
//                        functions
//----------------------------------------------------------

function containsVertice(classe , arrayIdsToTest) {
  var containVertice = false;
  for(var i = 0; i < arrayIdsToTest.length; i++){
    if(classe.includes(arrayIdsToTest[i])) {
      containVertice = true;
      break;
    }
  }
  return containVertice;
}

function addVerticesIdsToClass(classe, arrayVerticesIds) {
  for(var i = 0; i < arrayVerticesIds.length; i++){
    if(!classe.includes(arrayVerticesIds[i])) {
      classe.push(arrayVerticesIds[i]);
    }
  }
}

//Return les ids des page(s) pointée(s) par la page en paramètre
function getPointedVerticesIds(vertice, edges) {
  var pointedVerticesIds = [];
  for (var i = 0; i < edges.length; i++) {
    if (vertice.id == edges[i].id1) {
      pointedVerticesIds.push(edges[i].id2);
    }
  }
  return pointedVerticesIds;
}

function colorGraph(classeA, classeB, vertices){
  context.strokeStyle =  "#000000";
  context.lineWidth = 2;
  var vertice;

  for(var i = 0; i < classeA.length; i++){
    vertice = getVerticeById(classeA[i], vertices);

    context.beginPath();
    context.fillStyle = "#FF0000";
    
    context.arc(vertice.pos.x, vertice.pos.y, 10, 0, 2 * Math.PI);
    context.stroke();
    context.fill();
    context.closePath();
    context.beginPath();

    context.fillStyle = "#000000";  
    context.textBaseline = 'middle';
    context.textAlign = 'center';
    context.fillText(vertice.label, vertice.pos.x, vertice.pos.y);
    context.stroke();
    context.fill();
    context.closePath();
  }

  for(var i = 0; i < classeB.length; i++){
    vertice = getVerticeById(classeB[i], vertices);

    context.beginPath();
    context.fillStyle = "#00FF00";
    
    context.arc(vertice.pos.x, vertice.pos.y, 10, 0, 2 * Math.PI);
    context.stroke();
    context.fill();
    context.closePath();
    context.beginPath();

    context.fillStyle = "#000000";  
    context.textBaseline = 'middle';
    context.textAlign = 'center';
    context.fillText(vertice.label, vertice.pos.x, vertice.pos.y);
    context.stroke();
    context.fill();
    context.closePath();
  }
}



