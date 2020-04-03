<?php
/* Smarty version 3.1.33, created on 2019-10-06 14:56:19
  from 'C:\wamp64\www\tlial_tt\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\FilterResult.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9a0093881044_30832469',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '610766b20038e8b41e0dae13afd2fd1d2bf263ed' => 
    array (
      0 => 'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\FilterResult.tpl',
      1 => 1570373702,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d9a0093881044_30832469 (Smarty_Internal_Template $_smarty_tpl) {
?><table>
    <?php if (!empty($_smarty_tpl->tpl_vars['pathologies']->value)) {?><!--si le résultat n'est pas vide -->
    <tr>
        <th>Code Méridien</th><th>Nom Méridien</th><th>Type</th><th>Description</th>
    </tr>
        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['pathologies']->value, 'patho');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['patho']->value) {
?>
        <tr>
            <td><?php echo $_smarty_tpl->tpl_vars['patho']->value['code'];?>
</td>
            <td><?php echo $_smarty_tpl->tpl_vars['patho']->value['nom'];?>
</td>
            <td><?php echo $_smarty_tpl->tpl_vars['patho']->value['type'];?>
</td>
            <td><?php echo $_smarty_tpl->tpl_vars['patho']->value['desc'];?>
</td>
        </tr>
        <?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
    <?php } else { ?>
    <tr>
        <td>Aucun resultat trouvé</td>
    </tr>
    <?php }?>
</table><?php }
}
