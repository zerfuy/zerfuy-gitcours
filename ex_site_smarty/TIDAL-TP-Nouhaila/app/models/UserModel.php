<?php


class UserModel{

    private $conn = null;

    public function __construct(){ //permet de se connecter avec la BD
        
        $servername = "localhost";
        $username = "root";
        $password = "";
        $this->conn = new PDO("mysql:host=$servername;dbname=tli", $username, $password,    array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8"));
    }

    function login($login,$password){
        $user = null;

        $stmt = $this->conn->prepare("SELECT id_User,firstname FROM users WHERE login=:user AND password=:pass");
        $stmt->execute(['user'=>$login,'pass'=>$password]); 
        $user = $stmt->fetch();
        return $user;
    
    }

    function register($login,$pass,$fname,$lname){
        
        if (!preg_match("/^[a-zA-Z ]*$/",$login) || strlen($login) < 3) return null;
        if (!preg_match("/^[a-zA-Z ]*$/",$fname) || strlen($fname) < 3) return null;
        if (!preg_match("/^[a-zA-Z ]*$/",$lname) || strlen($lname) < 3) return null;
        if(strlen($pass) < 3) return null;

        $query = "INSERT INTO users(login,password,firstname,name) VALUES(:login,:pass,:fname,:lname)";
        $stmt = $this->conn->prepare($query);
        $result = $stmt->execute([
            'login'=>$login,
            'pass'=>$pass,
            'fname'=>$fname,
            'lname'=>$lname
        ]);
        echo "result : $result";
        if($result){
            $stmt = $this->conn->prepare("SELECT id_User,firstname FROM users WHERE login=:user AND password=:pass");
            $stmt->execute(['user'=>$login,'pass'=>$pass]); 
            $user = $stmt->fetch();
            return $user;
        }else{
            return null;
        }
    }


}