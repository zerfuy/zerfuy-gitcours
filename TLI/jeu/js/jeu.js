var id = document.getElementById("myCanvas");
var context = id.getContext("2d");
context.strokeStyle =  "#000000";
context.lineWidth = 10;
context.moveTo(0,0);
context.lineTo(300,400);
context.moveTo(300,0);
context.lineTo(0,400);
context.stroke();
