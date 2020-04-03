<?php
/* Smarty version 3.1.33, created on 2019-10-06 14:56:30
  from 'C:\wamp64\www\tlial_tt\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\RegisterView.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9a009e931246_06808361',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '873c46fa2dea7bc7ab46a0da0a5c92b8be955c7f' => 
    array (
      0 => 'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\RegisterView.tpl',
      1 => 1570373702,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
    'file:footer.tpl' => 1,
  ),
),false)) {
function content_5d9a009e931246_06808361 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
<div class="container">
    <form class="form" action="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/register" method="post">
        <h3 class="form-title">Inscription</h3>
        <table style="max-width:400px">
            <tr>
                <td>
                    <label>Prénom</label>
                </td>
                <td>
                    <input name="fname" value="<?php echo $_smarty_tpl->tpl_vars['form']->value['fname'];?>
" placeholder="Prénom" required>
                </td>
            <tr>
            <tr>
                <td>
                    <label>Nom</label>
                </td>
                <td>
                    <input name="lname" value="<?php echo $_smarty_tpl->tpl_vars['form']->value['lname'];?>
" placeholder="Nom" required>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Login</label>
                </td>
                <td>
                    <input name="login" value="<?php echo $_smarty_tpl->tpl_vars['form']->value['login'];?>
" placeholder="Login" required>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Mot de passe</label>
                </td>
                <td>
                    <input name="pass" type="password" value="<?php echo $_smarty_tpl->tpl_vars['form']->value['pass'];?>
" placeholder="Mot de passe" required>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <button id="submit" type="submit">S'inscrire</button>
                </td> 
            </tr> 
        </table> 
        <?php if (isset($_smarty_tpl->tpl_vars['error']->value)) {?>
        <small class="error"><?php echo $_smarty_tpl->tpl_vars['error']->value;?>
</small>
        <small class="info">Veuillez saisir obligatoirement le nom, prénom, login sous forme de caractère entre a et z.</small>
        <?php }?> 
    </form> 
</div> 
<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
}
}
