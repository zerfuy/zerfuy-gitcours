//import * as graphLib from './graphLib.js';
//TODO import correctement le FileSaver

var G;
window.onload = function start() {
  G = new Graph(false);// true = orienté
  restartChoiceAlgo(G);
}

const id = document.getElementById("myCanvas");
const graphModeButton = document.getElementById("graphMode");
const graphReinitButton = document.getElementById("graphReinit");
const graphExportButton = document.getElementById("graphExport");
const algoExecute = document.getElementById("algoExecute");
const selectAlgo = document.getElementById("algoSelect");
const context = id.getContext("2d");
const resAlgo = document.getElementById("resultAlgo");

var lastClickedVerticeId = -1;
var mousedownID = -1;
var draggedVerticleId = -1;
var mouseDragged = -1;

var NOalgo = ["Choose","Bipartition","Dijkstra"];
var Oalgo = ["Choose","PageRank","Dijkstra"];

  
/*G.addVerte(50, 50, "label1");
G.addVerte(100, 100, "label2");
G.addVerte(150, 150, "label3");
G.addVerte(200, 200, "label4");

var V = G.vertices;
G.addEdge(V[0], V[1]);
G.addEdge(V[2], V[3]);
pagerank(G);

updatePlan(G);
restartChoiceAlgo(G);*/

function updatePlan(graph) {

  //Configuration de l'affichage dans sa globalité 
  context.clearRect(0, 0, 1000, 1000);

  //edges
  if(graph.directed){
    updateEdgesArrowed(graph.edges, graph.vertices);  
  } else {
    updateEdges(graph.edges, graph.vertices);
  }
  //vertices
  updateVerticies("#ADD8E6", graph.vertices);
}

function updateVerticies(couleur, vertices){
  context.strokeStyle =  "#000000";
  context.lineWidth = 2;

  for(var i = 0; i < vertices.length; i++){
    
    context.beginPath();
    if(vertices[i].id == lastClickedVerticeId){
      context.fillStyle = "#FFFFFF";  
    } else {
      context.fillStyle = couleur;
    }
    context.arc(vertices[i].pos.x, vertices[i].pos.y, 10, 0, 2 * Math.PI);
    context.stroke();
    context.fill();
    context.closePath();
    context.beginPath();

    context.fillStyle = "#000000";  
    context.textBaseline = 'middle';
    context.textAlign = 'center';
    context.fillText(vertices[i].label, vertices[i].pos.x, vertices[i].pos.y);
    context.stroke();
    context.fill();
    context.closePath();
  }
}

function updateEdges(edges, vertices){
  context.strokeStyle =  "#000000";
  context.lineWidth = 2;

  for(var i = 0; i < edges.length; i++){
    var vertice1 = getVerticeById(edges[i].id1, vertices);
    var vertice2 = getVerticeById(edges[i].id2, vertices);

    if(vertice1 != -1 && vertice2 != -1){
      context.beginPath();
      context.moveTo(vertice1.pos.x,vertice1.pos.y);
      context.lineTo(vertice2.pos.x,vertice2.pos.y);
      context.stroke();
    }
  }
}

function updateEdgesArrowed(edges, vertices){

  context.strokeStyle =  "#000000";
  context.lineWidth = 2;

  for(var i = 0; i < edges.length; i++){
    var vertice1 = getVerticeById(edges[i].id1, vertices);
    var vertice2 = getVerticeById(edges[i].id2, vertices);

    if(vertice1 != -1 && vertice2 != -1){
      context.beginPath();
      drawArrow(context, vertice1.pos.x, vertice1.pos.y, vertice2.pos.x, vertice2.pos.y);
      context.stroke();
    }
  }
}
