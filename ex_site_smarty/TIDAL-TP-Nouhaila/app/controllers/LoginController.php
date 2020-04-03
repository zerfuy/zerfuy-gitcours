<?php

/**
 * URL = /login
 */

class Login{
    public function __construct()
    {
        if(isset($_SESSION['TIDAL_USER_ID'])){// si on est connecté on ne peut pas retaper /login elle nous emmène directement à page d'accueil
            header('location:'.$GLOBALS['project_path'].'/');// redirection à la page d'accueil
            exit;
        }

        include __DIR__ . "/../models/UserModel.php";//on fait appel à SearchModel 
        require_once __DIR__ . "/../../vendor/autoload.php";//on fait appel à Autoload pour utiliser SMARTY
        
        $model = new UserModel();
        $smarty = new Smarty();//on fait appel à la class SMARTY
        $smarty->setTemplateDir(__DIR__ . '/../views/');//définir le chemin des templates(Views)
        if(isset($_POST['login']) && isset($_POST['pass'])){//est ce que le mdp et login sont envoyés
            $login = $_POST['login'];
            $pass = $_POST['pass'];
            $user = $model->login($login,$pass);//il envoie login + mdp et récupère soit le USER soit null
            if($user != null){ // 
                $_SESSION['TIDAL_USER_ID'] = $user['id_User']; //l'id reste dans la session et ne disparait qu'après la deconnexion
                $_SESSION['TIDAL_USER_NAME'] = $user['firstname'];//le first name reste dans la session et ne disparait qu'après la deconnexion
                header('location:'.$GLOBALS['project_path'].'/search');//apres connexion, on part directement à la page recherche par mots clés
            }else{
                $smarty->assign('error','les informations  sont incorrects!!!'); 
            }
        }
        $smarty->assign('project_path',$GLOBALS['project_path']);
        $smarty->display('LoginView.tpl');

    }
}

?>