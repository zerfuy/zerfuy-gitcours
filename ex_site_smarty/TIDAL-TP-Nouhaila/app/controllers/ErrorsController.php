<?php

/**
 * URL = / (erors)
 */

class Errors{
    public function __construct()
    {
        require_once __DIR__ . "/../../vendor/autoload.php";//on fait appel à Autoload pour utiliser SMARTY   
        $smarty = new Smarty();//on fait appel à la class SMARTY
        $smarty->setTemplateDir(__DIR__ . '/../views/');//définir le chemin des templates(Views)
        $smarty->assign('project_path',$GLOBALS['project_path']); // on fait appel à project path à partir de la variable GLOBALS ET on l'envoie au template
        $smarty->display('Error.tpl');// afficher le tamplate (view)

    }
}

?>