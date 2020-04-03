<?php
<<<<<<< HEAD
/* Smarty version 3.1.33, created on 2019-10-05 18:29:48
=======
/* Smarty version 3.1.33, created on 2019-09-30 12:32:36
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
  from 'C:\wamp64\www\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\FilterView.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
<<<<<<< HEAD
  'unifunc' => 'content_5d98e11c8c37c8_80098679',
=======
  'unifunc' => 'content_5d91f5e44389e7_92724567',
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'a6cd4509ec1dde37ed4a4a02bf1ed96d70f51e3d' => 
    array (
      0 => 'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\FilterView.tpl',
<<<<<<< HEAD
      1 => 1570300183,
=======
      1 => 1569845631,
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
    'file:FilterResult.tpl' => 1,
    'file:footer.tpl' => 1,
  ),
),false)) {
<<<<<<< HEAD
function content_5d98e11c8c37c8_80098679 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>

<div class="container">
    <h2>List Pathologie</h2>

    <form class="form" action="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/filter" method="post" id="filterForm"><!-- Post permet de ne pas afficher dans l'URL -->
       
        <!--Tapper le nom de méridien  -->
        <input name="nom" value="" id="nom" placeholder="Le nom de méridien">
        <!-- categories -->
        <select name="category" id="category">
            <option value="0">Selectioner la categorie</option>
            <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['categories']->value, 'cat', false, 'index');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['index']->value => $_smarty_tpl->tpl_vars['cat']->value) {
?>
                <option value="cat_<?php echo $_smarty_tpl->tpl_vars['index']->value;?>
"><?php echo $_smarty_tpl->tpl_vars['cat']->value['name'];?>
=======
function content_5d91f5e44389e7_92724567 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>

<div class="filter-container">
    <h2>List Pathologie</h2>

    <form action="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/filter" method="post" id="filterForm"><!-- Post permet de ne pas afficher dans l'URL -->
        <!--Tapper le nom de méridien  -->
        <input name="nom" value="" id="nom" placeholder="Le nom de méridien">
        <!-- List des types des pathologies -->
        <select name="type" id="type">
            <option value="0" selected>Selectioner le type</option>
            <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['pathologies']->value, 'patho');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['patho']->value) {
?>
                <option value="<?php echo $_smarty_tpl->tpl_vars['patho']->value['type'];?>
"><?php echo $_smarty_tpl->tpl_vars['patho']->value['type'];?>
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
</option>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
        </select>
<<<<<<< HEAD
        <select name="caracteristique" id="caracteristique">
        <option value="0">Selectioner le caractéristique</option>
        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['categories']->value, 'cat', false, 'index');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['index']->value => $_smarty_tpl->tpl_vars['cat']->value) {
?>
            <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['cat']->value['values'], 'val');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['val']->value) {
?>
                <option class="opt cat_<?php echo $_smarty_tpl->tpl_vars['index']->value;?>
" value="<?php echo $_smarty_tpl->tpl_vars['val']->value;?>
" style="display:none"><?php echo $_smarty_tpl->tpl_vars['val']->value;?>
=======
        <!--lister des caractéristiques  -->
        <select name="caracteristique" id="caracteristique">
            <option value="0" selected>Selectioner la caractéristique</option>
            <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['caracts']->value, 'crt');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['crt']->value) {
?>
                <option value="<?php echo $_smarty_tpl->tpl_vars['crt']->value;?>
"><?php echo $_smarty_tpl->tpl_vars['crt']->value;?>
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
</option>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
<<<<<<< HEAD
        <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
=======
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
        </select>
        <!-- le bouton recherche -->
        <button type="submit">Recherche</button>
    </form>
    <!-- le résultat de la recherche qui représente le tableau, on peut le voir dans FilterResult.tpl  -->
    <div id="result">
        <?php $_smarty_tpl->_subTemplateRender("file:FilterResult.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
    </div>
  </div>
<<<<<<< HEAD
=======
  <!-- On appelle la biliotheque JQUERY (Bibliotheque de JS)  -->
  <?php echo '<script'; ?>
 src="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/js/jquery-3.4.1.min.js"><?php echo '</script'; ?>
>
>>>>>>> 552ec70abc1f907b0a21ebc388d556b823ff3a2d
  <?php echo '<script'; ?>
 src="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/js/filter.js"><?php echo '</script'; ?>
>

<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>




<?php }
}
