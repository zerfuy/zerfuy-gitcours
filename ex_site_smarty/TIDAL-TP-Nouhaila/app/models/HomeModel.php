<?php


class HomeModel{

    private $conn = null;

    public function __construct(){ //permet de se connecter avec la BD
        $servername = "localhost";
        $username = "root";
        $password = "";
        $this->conn = new PDO("mysql:host=$servername;dbname=tli", $username, $password,    array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));
    }

    public function getRss(){

        $pathos = $this->conn->query('SELECT `desc` FROM patho LIMIT 10')->fetchAll();//recupérer les données de la BD 
        $meridiens = $this->conn->query('SELECT nom FROM meridien LIMIT 10')->fetchAll();
        $symptomes = $this->conn->query('SELECT `desc` FROM symptome LIMIT 10')->fetchAll();
        
        return [
            "pathos"=>$pathos,
            "meridiens"=>$meridiens,
            "symptomes"=>$symptomes
        ];
    }

}