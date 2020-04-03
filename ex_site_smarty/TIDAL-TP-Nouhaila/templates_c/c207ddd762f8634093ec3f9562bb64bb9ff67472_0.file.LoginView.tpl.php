<?php
/* Smarty version 3.1.33, created on 2019-10-04 13:52:45
  from 'C:\wamp64\www\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\LoginView.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d974ead8915d6_58934338',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'c207ddd762f8634093ec3f9562bb64bb9ff67472' => 
    array (
      0 => 'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\LoginView.tpl',
      1 => 1570174255,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
    'file:footer.tpl' => 1,
  ),
),false)) {
function content_5d974ead8915d6_58934338 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
<div class="container">
    <form class="form login" action="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/login" method="post">
        <h3 class="form-title">Connexion</h3>
        <input name="login" value="" placeholder="Login">
        <input name="pass" value="" placeholder="Mot de passe">
        <button id="submit" type="submit">Se connecter</button>
        <?php if (isset($_smarty_tpl->tpl_vars['error']->value)) {?>
        <small class="error"><?php echo $_smarty_tpl->tpl_vars['error']->value;?>
</small>
        <?php }?>
    </form>
</div>
<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
}
}
