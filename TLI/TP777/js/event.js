graphExportButton.onclick = function(event) {
  exportJSON(G);
  updatePlan(G);
}

graphModeButton.onclick = function(event) {
  G.directed = !G.directed
  restartChoiceAlgo(G);
  updatePlan(G);
}

graphReinitButton.onclick = function(event) {
  reinitialisationGraph(G);
  updatePlan(G);
}

algoExecute.onclick = function(event) {
  updatePlan(G);
  executeAlgo();
}

document.onkeydown = function(event) {
  var nomTouche = event.key;
  if (nomTouche == 'Delete' && lastClickedVerticeId != -1){
    G.deleteVertice(lastClickedVerticeId);
    lastClickedVerticeId = -1;
  }
  updatePlan(G);
}

id.onmousedown = function(event) {
  event = event || window.event;
  event.preventDefault();
  mousedownID = 1;
  var posXMouse = event.pageX - this.offsetLeft;
  var posYMouse = event.pageY - this.offsetTop;
  var targetId = G.isCoordOnVertice(posXMouse, posYMouse);
  draggedVerticleId = targetId;

  //clear algorithm output
  while (resAlgo.firstChild) {
    resAlgo.removeChild(resAlgo.firstChild);
  }
  updatePlan(G);
}

id.ondblclick = function(event) {
  event = event || window.event;
  event.preventDefault();
  var posXMouse = event.pageX - this.offsetLeft;
  var posYMouse = event.pageY - this.offsetTop;
  var targetId = G.isCoordOnVertice(posXMouse, posYMouse);
  var vertice = G.getVerticeById(draggedVerticleId);
  var newLabel = prompt("new label ?", vertice.label);
  if(newLabel == null){
    newLabel = vertice.label;
  }
  vertice.label = newLabel;
  updatePlan(G);
}

id.onmousemove = function(event) {
  event = event || window.event;
  event.preventDefault();
  if(mousedownID == 1 && draggedVerticleId != -1){
    var posXMouse = event.pageX - this.offsetLeft;
    var posYMouse = event.pageY - this.offsetTop;
    var vertice = G.getVerticeById(draggedVerticleId);
    vertice.pos.x = posXMouse;
    vertice.pos.y = posYMouse;
    mouseDragged = 1;
    updatePlan(G);
  }
}

id.onmouseup = function(event) {
  event = event || window.event;
  event.preventDefault();
  mousedownID = -1;
  if(mouseDragged == 1) {
    mouseDragged = -1;
    draggedVerticleId = -1;
  } else {
    var posXMouse = event.pageX - this.offsetLeft;
    var posYMouse = event.pageY - this.offsetTop;
    var targetId = G.isCoordOnVertice(posXMouse, posYMouse);

    if(targetId == -1) {
      //if click wasn't on existing Vertice
      G.addVerte(posXMouse,posYMouse,"")
    } else {
      //déselectionne
      if(lastClickedVerticeId == targetId) {
        lastClickedVerticeId = -1;
      //relie
      } else if(lastClickedVerticeId != -1) {
        var edge = {
          id1 : lastClickedVerticeId,
          id2 : targetId,
        }
        if(!G.directed) {
          if(G.edgeAlreadyExistsInAny(edge) != 1){
            G.addEdge(G.getVerticeById(lastClickedVerticeId), G.getVerticeById(targetId));
          }else{
            G.deleteEdge(lastClickedVerticeId, targetId);
            G.deleteEdge(lastClickedVerticeId, targetId);
          }
          lastClickedVerticeId = -1;
        } else {
          if(G.edgeAlreadyExistsIn(edge) != 1) {
            G.addEdge(G.getVerticeById(lastClickedVerticeId), G.getVerticeById(targetId));
          } else {
            G.deleteEdge(lastClickedVerticeId, targetId);
          }
          lastClickedVerticeId = -1;
        }
      //sélectionne
      } else {
        lastClickedVerticeId = targetId;
      }
    } 
  }
  updatePlan(G);
}