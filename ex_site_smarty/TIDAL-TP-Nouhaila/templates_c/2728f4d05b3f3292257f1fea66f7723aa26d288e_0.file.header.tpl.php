<?php
/* Smarty version 3.1.33, created on 2019-10-06 14:56:04
  from 'C:\wamp64\www\tlial_tt\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9a00845a1f16_07753327',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '2728f4d05b3f3292257f1fea66f7723aa26d288e' => 
    array (
      0 => 'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\header.tpl',
      1 => 1570373702,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d9a00845a1f16_07753327 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_checkPlugins(array(0=>array('file'=>'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\vendor\\smarty\\smarty\\libs\\plugins\\modifier.date_format.php','function'=>'smarty_modifier_date_format',),));
?>
<!DOCTYPE html>
<html lang="fr">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta charset="UTF-8">
<link href="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/css/style.css" rel="stylesheet" type="text/css" />
<title> Ca pique mais c'est bon ! </title>
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
}
