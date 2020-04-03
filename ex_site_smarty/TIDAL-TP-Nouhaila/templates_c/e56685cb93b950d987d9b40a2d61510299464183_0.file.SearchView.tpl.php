<?php
/* Smarty version 3.1.33, created on 2019-10-04 13:52:45
  from 'C:\wamp64\www\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\SearchView.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d974eadae31d0_02791975',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'e56685cb93b950d987d9b40a2d61510299464183' => 
    array (
      0 => 'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\SearchView.tpl',
      1 => 1570174263,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
    'file:SearchResult.tpl' => 1,
    'file:footer.tpl' => 1,
  ),
),false)) {
function content_5d974eadae31d0_02791975 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>

<div class="container">
    <h2>Recherche Par mot clé</h2>

    <div class="form">
        <input name="nom" value="" id="keyword" placeholder="Le mot clé">
        <button id="submit" type="submit">Recherche</button>
    </div>

    <div id="result" class="search">
      <?php $_smarty_tpl->_subTemplateRender('file:SearchResult.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
    </div>
</div>
<?php echo '<script'; ?>
 src="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/js/search.js"><?php echo '</script'; ?>
>
<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
}
}
