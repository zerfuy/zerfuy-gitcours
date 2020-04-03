<?php
session_start();
// index.php?url={var}
$project_path = str_replace('\\', '/', dirname(__FILE__));//remplacer les anti slachs par les slachs dans le chemin de projet
$project_path = str_replace($_SERVER["DOCUMENT_ROOT"],"",$project_path);//on enlève le chamin de localhost (tous ce qui a avnt www)

$url = isset($_GET['url']) ? $_GET['url'] : 'home';//s'il n'exsite pas le dernier URL, on utilise HOME par défaut
$url = rtrim($url, '/');//enlève les / ajoutées à la fin 
// a/b/c => $url[0]:a, $url[1]:b ...
$url = explode('/', $url);//voir fichier WORD
//
$controller = ucfirst($url[0]) . "Controller.php";
// ucfirst : permet de rendre le premier caractèer en majuscule
if( file_exists("app/controllers/$controller") ){
    // Si le fichier app/controllers/{url}Controller.php exists
    include "app/controllers/$controller"; //on appelle le fichier
    $class = ucfirst($url[0]);
    new $class(); //eg: new Filter(), appel à la classe Filter qui se trouve dans FilterController.php
}else{
    // Sinon
    include "app/controllers/ErrorsController.php";
    new Errors();
}