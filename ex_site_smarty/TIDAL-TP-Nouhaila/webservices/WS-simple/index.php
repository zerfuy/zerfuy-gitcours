<?php

$project_location = "/TIDAL-Webservice/WS-simple";
// index.php?url={var}
if(isset($_GET['url'])){ //il voit est ce qu'il y a le paramètre URL dans le lien
    $url = $_GET['url'];//ramène l'URL
    $url = rtrim($url, '/');//enlève les / ajoutées à la fin 
    $url = explode('/', $url);//voir fichier WORD
    //adresse_site/calculatrice/[opération]/nombre1/nombre2
    if($url[0] == 'calculatrice'){


        // — addition de deux entiers ;
        // — soustraction de deux entiers ;
        // — multiplication de deux entiers ;
        // — division de deux entiers

        if(isset($url[1]) && in_array($url[1],["addition","soustraction","multiplication","division"]) ){
            if( isset($url[2]) && isset($url[3]) ){//isset permet de dire est ce que les parametres 2 et 3 existent

                if (preg_match('/^[0-9]+$/', $url[2]) && preg_match('/^[0-9]+$/', $url[3]) ) {
                    //l'utiisation de regular expression qui permet de dire que les 2 paramètres devront être 2 nombres entiers 

                    switch($url[1]){
                        case "addition" : echo $url[2] + $url[3];break;
                        case "soustraction" : echo $url[2] - $url[3];break;
                        case "multiplication" : echo $url[2] * $url[3];break;
                        case "division" : echo ($url[3] != 0) ? $url[2] / $url[3] : ' Erreur de division, on ne peut pas avoir au dénominateur 0  '  ;break;
                    }

                }else{
                    //echo "Il faut que les paramètres soient des nombres ";
                    header("Location:$project_location/404.php");
                }

            }else{
                //echo "Obligation d'avoir 2 numéros";
                header("Location:$project_location/404.php");
            }
        }else{
            //echo "aucune operation trouvé";
            header("Location:$project_location/404.php");
        }

    }else{
        //echo "Lien introuvable";
        header("Location:$project_location/404.php");
    }


}else{
    header("Location:$project_location/404.php");//rewriting en php
}