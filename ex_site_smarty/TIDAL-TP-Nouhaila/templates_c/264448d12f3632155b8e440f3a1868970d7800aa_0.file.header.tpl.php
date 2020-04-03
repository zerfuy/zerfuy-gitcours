<?php
<<<<<<< HEAD
/* Smarty version 3.1.33, created on 2019-10-04 13:52:09
=======
/* Smarty version 3.1.33, created on 2019-09-30 12:32:36
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
  from 'C:\wamp64\www\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
<<<<<<< HEAD
  'unifunc' => 'content_5d974e89d13a97_26111796',
=======
  'unifunc' => 'content_5d91f5e451a989_96525010',
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '264448d12f3632155b8e440f3a1868970d7800aa' => 
    array (
      0 => 'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\header.tpl',
<<<<<<< HEAD
      1 => 1570174249,
=======
      1 => 1569845631,
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
<<<<<<< HEAD
function content_5d974e89d13a97_26111796 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_checkPlugins(array(0=>array('file'=>'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\vendor\\smarty\\smarty\\libs\\plugins\\modifier.date_format.php','function'=>'smarty_modifier_date_format',),));
?>
<!DOCTYPE html>
=======
function content_5d91f5e451a989_96525010 (Smarty_Internal_Template $_smarty_tpl) {
?><!DOCTYPE html>
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
<html lang="fr">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="UTF-8">
<link href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/css/style.css" rel="stylesheet" type="text/css" />
<title> Ca pique mais c'est bon ! </title>
<<<<<<< HEAD
<!-- On appelle la biliotheque JQUERY (Bibliotheque de JS)  -->
<?php echo '<script'; ?>
 src="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/js/jquery-3.4.1.min.js"><?php echo '</script'; ?>
>
</head>
<body>
<div class="navbar">
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/" class="<?php if (!isset($_GET['url'])) {?>active<?php }?>">Accueil</a>
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/search" class="<?php if (isset($_GET['url']) && $_GET['url'] == 'search') {?>active<?php }?>">Recherche</a>
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/filter" class="<?php if (isset($_GET['url']) && $_GET['url'] == 'filter') {?>active<?php }?>">Pathologie</a>
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/info" class="<?php if (isset($_GET['url']) && $_GET['url'] == 'info') {?>active<?php }?>">Informations</a> 

  <?php if (isset($_SESSION['TIDAL_USER_ID'])) {?>
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/logout">déconnexion</a>
  <?php } else { ?>
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/register" class="<?php if (isset($_GET['url']) && $_GET['url'] == 'register') {?>active<?php }?>">Inscription</a>
  <a href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/login" class="<?php if (isset($_GET['url']) && $_GET['url'] == 'login') {?>active<?php }?>">Connexion</a>
  <?php }?>


</div>
<?php if (isset($_SESSION['TIDAL_USER_ID'])) {?>
<p class="user-name">
<?php if (smarty_modifier_date_format(time(),"%H") > 4 && smarty_modifier_date_format(time(),"%H") < 18) {?>
Bonjour
<?php } else { ?>
Bonsoir
<?php }?>

<b><?php echo $_SESSION['TIDAL_USER_NAME'];?>
</b> vous êtes connecté!</p>
<?php }
}
=======
</head>
<body>
<div id="Sidenav1" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="../index.php" id="linkAccueil">Accueil</a>
  <a href="../Connexion.php" id="linkConnexion">Connexion</a>
  <a href="../Informations.php" id="linkInformations">Informations</a> 
  <a href="./filter">Pathologie</a> 
</div>
<div id="menubar">
    <span  id="openMenuBtn" onclick="openNav()">&#9776; Menu</span>
  </div><?php }
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
}
