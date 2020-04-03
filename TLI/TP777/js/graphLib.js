// Fonctions Vérfiées (voir celle à mettre dans graph.js en méthode)
function getVerticeById(idToFind, vertices) {
  var vertice = -1;
  for(var i = 0; i < vertices.length; i++){
    if(vertices[i].id == idToFind){
      vertice = vertices[i];
    }
  }
  return vertice;
}

function reinitialisationGraph (graph) {
  graph.reinit();
  lastClickedVerticeId = -1;
  mousedownID = -1;
  draggedVerticleId = -1;
  mouseDragged = -1;
}

function drawArrow(context, fromx, fromy, tox, toy){
  var headlen = 13;

  distx = Math.sqrt((fromx-tox)*(fromx-tox))/10;
  disty = Math.sqrt((fromy-toy)*(fromy-toy))/10;

  if(fromx < tox - 20){
    tox = tox - 8;
  }else if (fromx > tox + 20) {
    tox = tox + 8;
  }

  if(fromy < toy -20){
    toy = toy - 8;
  }else if (fromy > toy + 20) {
    toy = toy + 8;
  }

  var angle = Math.atan2(toy-fromy,tox-fromx);
  context.moveTo(fromx, fromy);
  context.lineTo(tox, toy);
  context.lineTo(tox-headlen*Math.cos(angle-Math.PI/6),toy-headlen*Math.sin(angle-Math.PI/6));
  context.moveTo(tox, toy);
  context.lineTo(tox-headlen*Math.cos(angle+Math.PI/6),toy-headlen*Math.sin(angle+Math.PI/6));
}

function restartChoiceAlgo (graph) {
  removeSelectOption ();
  if(graph.directed) {
    setValueSelectAlgo(Oalgo);
  } else {
    setValueSelectAlgo(NOalgo);
  }
}

function setValueSelectAlgo (arrayValue){
  for(var i = 0; i < arrayValue.length; i++){
    var option = document.createElement('option');
    option.appendChild(document.createTextNode(arrayValue[i]));
    option.value = arrayValue[i];
    selectAlgo.appendChild(option);
  }
}

function removeSelectOption () {
  var length = selectAlgo.options.length;
  for (var i=length; i > 0; i--) {
    par = selectAlgo.options[i-1].parentNode;
    par.removeChild( selectAlgo.options[i-1] );
  }
}

function executeAlgo () {
  if (selectAlgo.value == "PageRank") {
    pagerank(G);
  } else if (selectAlgo.value == "Bipartition") {
    isBipartite(G);
  } else if (selectAlgo.value == "Dijkstra") {
    dijkstra(G);
  }
}
