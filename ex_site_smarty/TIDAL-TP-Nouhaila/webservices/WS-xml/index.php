<?php


/* 

Récupérer la liste des pathologies à partir de son type ou son IDP
Exemple 1 : ?idP=3
Exemple 2 : ?type=lp
Exemple 3 : ?idP=3&type=lp

 */



header("Content-Type: application/xml; charset=utf-8"); // Afficher le contenu sous format XML

$servername = "localhost";
$username = "root";
$password = "";
$conn = new PDO("mysql:host=$servername;dbname=tli", $username, $password,    array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));


$idP  = isset($_GET['idP']) ? $_GET['idP'] : '0';
$type  = isset($_GET['type']) ? $_GET['type'] : '0';

$query = "SELECT *  FROM patho WHERE 1=1 "; // on a mis WHERE 1=1 vu qu'on peut pas s'arreter dans FROM et c'est une logique qui évite les erreurs

if($idP != "0") $query .= " AND patho.idP = $idP";
if($type != "0") $query .= " AND patho.type = '$type'";

$stmt = $conn->query($query);
$pathologies = $stmt->fetchAll();

echo '<?xml version="1.0" encoding="UTF-8"?><listpathologies>';
foreach($pathologies as $pathologie){// ramener les pathologies 1 par 1
    echo "<patho>";
    foreach($pathologie as $key=>$value){ // ramener les key et leurs values 1 par 1
        if( !is_numeric($key) ){ // si le key n'est pas nombre
            // <idP> : 
            echo "<". htmlspecialchars($key).">";//on écrit l'élément XML
            // 109
            echo htmlspecialchars($value);//on écrit la valeur de l'élément XML
            // </idP>
            echo "</". htmlspecialchars($key).">";//on ferme l'élément </idp>
        }
    }
    echo "</patho>";
}
echo '</listpathologies>';