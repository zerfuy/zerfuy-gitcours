<?php
/* Smarty version 3.1.33, created on 2019-10-06 14:56:19
  from 'C:\wamp64\www\tlial_tt\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\FilterView.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9a00937e54f9_99288842',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6cef79ee94dc96841f526aebf2b9175254bd6353' => 
    array (
      0 => 'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\FilterView.tpl',
      1 => 1570373702,
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
function content_5d9a00937e54f9_99288842 (Smarty_Internal_Template $_smarty_tpl) {
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
</option>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
        </select>
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
</option>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
        <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
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
  <?php echo '<script'; ?>
 src="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/js/filter.js"><?php echo '</script'; ?>
>

<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>




<?php }
}
