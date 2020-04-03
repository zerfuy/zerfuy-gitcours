class Graph {
  constructor(directed) {
    this._vertices = [];
    this._edges = [];
    this._directed = directed;
    this._verticeCount = 0;
  }

  reinit() {
    this._vertices = [];
    this._edges = [];
    this._directed = false;
    this._verticeCount = 0;
  }

  getVerticeById(idToFind) {
    var vertice = -1;
    for(var i = 0; i < this._vertices.length; i++){
      if(this._vertices[i].id == idToFind){
        vertice = this._vertices[i];
      }
    }
    return vertice;
  }

  getIndexVerticeById(id) {
    var index;
    for(var i = 0; i < this._vertices.length; i++){
      if(this._vertices[i].id == id){
        index = i;
      }
    }
    return index;
  } 

  deleteVertice(id) {// id ou vertice ? ou les deux ?
    var index = this.getIndexVerticeById(id);
    this._vertices.splice(index, 1);

    for(var i = 0; i < this._edges.length; i++){
      if(this._edges[i].id1 == id || this._edges[i].id2 == id){
        this._edges.splice(i, 1);
      }
    }
  }

  deleteEdge(id1, id2) {
    for(var i = 0; i < this._edges.length; i++){
      if((this._edges[i].id1 == id1 && this._edges[i].id2 == id2) || (this._edges[i].id1 == id2 && this._edges[i].id2 == id1)){
        this._edges.splice(i, 1);
      }
    }
  }

  // 2 sides
  edgeAlreadyExistsInAny(edge){
    for(var i = 0; i < this._edges.length; i++){
      if((this._edges[i].id1 == edge.id1 && this._edges[i].id2 == edge.id2) || (this._edges[i].id1 == edge.id2 && this._edges[i].id2 == edge.id1)){
        return 1;
      }
    }
  }

  //exact equality
  edgeAlreadyExistsIn(edge){
    var returnValue = -1;
    for(var i = 0; i < this._edges.length; i++){
      if(this._edges[i].id1 == edge.id1 && this._edges[i].id2 == edge.id2){
        returnValue = 1;
      }
    }
    return returnValue;
  }

  isCoordOnVertice(x, y) {
    for(var j = 0; j < this._vertices.length; j++){
      var x0 = this._vertices[j].pos.x;
      var y0 = this._vertices[j].pos.y;
      if( Math.sqrt((x-x0)*(x-x0) + (y-y0)*(y-y0)) < 12 ) {
        return this._vertices[j].id;
      }
    }
    return -1;
  }

  //---------------------
  // getters and setters
  //---------------------
  addVerte(posx, posy, label) {
    if(label == ""){
      label = "x";
    }

    var position = {
      x : posx,
      y : posy,
    }

    var Vertice = {
      id : this._verticeCount,
      label : label,
      pos : position,
    }

    this._verticeCount++;
    this._vertices.push(Vertice);
  }

  addEdge(vertice1, vertice2) {
    var Edge = {
      id1 : vertice1.id,
      id2 : vertice2.id,
    }

    this._edges.push(Edge);
  }

  get vertices() {
  	return this._vertices;
  }

  get edges() {
  	return this._edges;
  }

  get directed() {
    return this._directed;
  }

  get verticeCount() {
    return this._verticeCount;
  }

  set vertices(value) {
    this._vertices = value;
  }

  set edges(value) {
    this._edges = value;
  }

  set directed(value) {
    this._directed = value;
  }

  set verticeCount(value) {
    this._verticeCount = value;
  }
}