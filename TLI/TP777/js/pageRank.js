
function pagerank(graph) {

  var vertices = graph.vertices;
  var verticesPageRank = [];
  var scores = initScores(vertices);
  var ancienScores = {};
  
  console.log(scores);
  var cptPointedByverticePointingToVerticeId = 0;
  var continuer = true; 

  ct = 0;
  while((continuePageRank(ancienScores, scores, vertices) && ct < 20) || (ct == 0)){
    ct++;
    
    for(var i = 0; i < vertices.length; i++){
      ancienScores[vertices[i].id] = scores[vertices[i].id];
    }

    for(var i = 0; i < vertices.length; i++){
      Vertice = vertices[i];
      verticesPointingToVerticeIds = getPointingToVertices(Vertice, edges);
      var newpagerank = 0;
      for(var j = 0; j < verticesPointingToVerticeIds.length; j++){
        verticePointingToVerticeId = verticesPointingToVerticeIds[j];
        cptPointedByverticePointingToVerticeId = getPointedVerticesCount(getVerticeById(verticePointingToVerticeId, vertices), edges);
        newpagerank = newpagerank + ancienScores[verticePointingToVerticeId]/cptPointedByverticePointingToVerticeId;
        scores[Vertice.id] = newpagerank;
      } 
      //console.log('Vertice.id, newpagerank : ' + Vertice.label + ', ' + newpagerank);
    }
    //console.log(scores);
    console.log('itération ' + ct);
  }

  for(var i = 0; i < vertices.length; i++){
    var para = document.createElement("p");
    var strResult = "";
    strResult += vertices[i].id;
    strResult += " : ";
    strResult += scores[vertices[i].id];
    strResult += "\n";
    para.innerHTML = strResult;
    resAlgo.appendChild(para);
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

//Return les ids des page(s) qui pointent la page en paramètre
function getPointingToVertices(vertice, edges) {
  var pointingVerticesIds = [];
  for (var i = 0; i < edges.length; i++) {
    if (vertice.id == edges[i].id2) {
      pointingVerticesIds.push(edges[i].id1);
    }
  }
  return pointingVerticesIds;
}

//Return le nombre de page(s) pointée(s) par la page en paramètre
function getPointedVerticesCount(vertice, edges) {
  var count = 0;
  for (var i = 0; i < edges.length; i++) {
    if (vertice.id == edges[i].id1) {
      count++;
    }
  }
  return count;
}

//exception si tableaux de tailles différentes
function dotProduct(ancienScores, scores, len) {
  var result = 0;
  for(var i = 0; i < len ; i++){
    result = result + (ancienScores[i])*(scores[i]);
  }
  return result;
}

function getNorme(tab, len) {
  var result = 0;
  for(var i = 0; i < len ; i++){
    result = result + (tab[i])*(tab[i]);
  }
  return Math.sqrt(result);
}

function continuePageRank(ancienScores, scores, vertices){
  console.log('ancienScores');
  for(var i = 0; i < vertices.length; i++){
    console.log(ancienScores[vertices[i].id]);
  }
  console.log('scores');
  for(var i = 0; i < vertices.length; i++){
    console.log(scores[vertices[i].id]);
  }
  var dP = dotProduct(ancienScores, scores, vertices.length);
  var sM = getNorme(ancienScores, vertices.length) * getNorme(scores, vertices.length);

  console.log("dP/sM : " + dP/sM);
  return dP/sM < 0.999999;
}

function initScores (vertices) {
  scores = {};
  firstpagerank = 1/vertices.length;
  for(var i = 0; i < vertices.length; i++){
    scores[vertices[i].id] = firstpagerank;
  }
  return scores;
}

