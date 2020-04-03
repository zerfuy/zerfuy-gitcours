<?php

/**
 * URL = /search
 */

class Search{
    public function __construct()
    {

        if(!isset($_SESSION['TIDAL_USER_ID'])){
            header('location:'.$GLOBALS['project_path'].'/login');
            exit;
        }

        include __DIR__ . "/../models/SearchModel.php";//on fait appel à SearchModel 
        require_once __DIR__ . "/../../vendor/autoload.php";//on fait appel à Autoload pour utiliser SMARTY
        
        $smarty = new Smarty();//on fait appel à la class SMARTY
        $smarty->setTemplateDir(__DIR__ . '/../views/');//définir le chemin des templates(Views)
        $smarty->assign('project_path',$GLOBALS['project_path']);
        $model= new SearchModel();
        if(isset($_POST['keyword'])){
            $string = $_POST['keyword'];
            $pathologies = $model->getPathosByKeyword($string);
            $smarty->assign("pathologies",$pathologies);
            $smarty->display('SearchResult.tpl');
        }else{
            $pathologies = $model->getPathosByKeyword("");
            $smarty->assign("pathologies",$pathologies);
            $smarty->display('SearchView.tpl');
        }

    }
}

?>