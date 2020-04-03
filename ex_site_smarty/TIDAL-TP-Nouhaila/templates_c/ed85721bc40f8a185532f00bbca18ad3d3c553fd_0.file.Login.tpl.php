<?php
/* Smarty version 3.1.33, created on 2019-09-30 23:41:21
  from 'C:\wamp64\www\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\Login.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9292a10ae385_13115496',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'ed85721bc40f8a185532f00bbca18ad3d3c553fd' => 
    array (
      0 => 'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\Login.tpl',
      1 => 1569886849,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
    'file:footer.tpl' => 1,
  ),
),false)) {
function content_5d9292a10ae385_13115496 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
<div class="container">
    <form class="form" action="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/login" method="post">
        <h3 class="form-title">Connexion</h3>
        <input name="login" value="" placeholder="Login">
        <input name="pass" value="" placeholder="Mot de passe">
        <button id="submit" type="submit">Se connecter</button>
    </form>

</div>
<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
}
}
