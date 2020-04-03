<?php

/**
 * URL = /    ou /home
 */

class Home{
    public function __construct()
    {
        include __DIR__ . "/../models/HomeModel.php";//on fait appel au fichier HomeModel.php 
        require_once __DIR__ . "/../../vendor/autoload.php";//on fait appel à Autoload pour utiliser SMARTY et autoload permet de définir toutes les bibliotheques presentes dans vendor 

        $model = new HomeModel();// on fait appel à la classe HomeModel qui se trouve dans le fichier HomeModel.php 
        $rss = $model->getRss();//le controleur demande et récupère  les données du model

        $smarty = new Smarty();//on fait appel à la class SMARTY
        $smarty->setTemplateDir(__DIR__ . '/../views/');//définir le chemin des templates(Views)
        $smarty->assign('project_path',$GLOBALS['project_path']);//Attibuer project_path dans VIEW
        $smarty->assign('rss',$rss);//Attribuer les données à View
        $smarty->display('HomeView.tpl');// Afficher la VIEW
    }
}

?>