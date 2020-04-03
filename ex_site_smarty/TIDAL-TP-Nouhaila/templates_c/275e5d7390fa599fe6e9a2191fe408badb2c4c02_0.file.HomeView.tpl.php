<?php
/* Smarty version 3.1.33, created on 2019-10-06 14:56:04
  from 'C:\wamp64\www\tlial_tt\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\HomeView.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9a00844f0f08_28205050',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '275e5d7390fa599fe6e9a2191fe408badb2c4c02' => 
    array (
      0 => 'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\HomeView.tpl',
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
function content_5d9a00844f0f08_28205050 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender('file:header.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
?>
<div class="container">
    <h2>TIDAL TP PROJECT</h2>
<div class="cover">
<?php if (!isset($_SESSION['TIDAL_USER_ID'])) {?>
        <form class="form login" action="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/login" method="post">
        <h3 class="form-title">Connexion</h3>
        <input name="login" value="" placeholder="Login">
        <input name="pass" value="" placeholder="Mot de passe">
        <button id="submit" type="submit">Se connecter</button>
    </form>
<?php }?>
</div>

<div class="cards">
    <div class="card">
        <h4>Liste des méridiens</h4>
        <ul>
                        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['rss']->value['meridiens'], 'mer');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['mer']->value) {
?>
            <li><?php echo $_smarty_tpl->tpl_vars['mer']->value['nom'];?>
</li>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
        </ul>
    </div>

    <div class="card">
        <h4>Liste des pathologies</h4>
        <ul>
            <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['rss']->value['pathos'], 'patho');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['patho']->value) {
?>
            <li><?php echo $_smarty_tpl->tpl_vars['patho']->value['desc'];?>
</li>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
        </ul>
    </div>

    <div class="card">
        <h4>Liste des symptômes</h4>
        <ul>
            <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['rss']->value['symptomes'], 'sym');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['sym']->value) {
?>
            <li><?php echo $_smarty_tpl->tpl_vars['sym']->value['desc'];?>
</li>
            <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
        </ul>
    </div>
</div>


</div>
<?php $_smarty_tpl->_subTemplateRender('file:footer.tpl', $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array(), 0, false);
}
}
