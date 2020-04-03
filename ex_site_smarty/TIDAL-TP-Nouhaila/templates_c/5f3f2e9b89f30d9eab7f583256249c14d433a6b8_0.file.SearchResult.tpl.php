<?php
/* Smarty version 3.1.33, created on 2019-10-04 13:52:45
  from 'C:\wamp64\www\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\SearchResult.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d974eadb313d5_36926720',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '5f3f2e9b89f30d9eab7f583256249c14d433a6b8' => 
    array (
      0 => 'C:\\wamp64\\www\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\SearchResult.tpl',
      1 => 1570174260,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d974eadb313d5_36926720 (Smarty_Internal_Template $_smarty_tpl) {
?><table>
    <?php if (!empty($_smarty_tpl->tpl_vars['pathologies']->value)) {?><!--si le résultat n'est pas vide -->
    <tr>
        <th>Id Pathologie</th><th>Méridien</th><th>Type</th><th>Description</th>
    </tr>
        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['pathologies']->value, 'patho');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['patho']->value) {
?>
        <tr>
            <td><?php echo $_smarty_tpl->tpl_vars['patho']->value['idP'];?>
</td>
            <td><?php echo $_smarty_tpl->tpl_vars['patho']->value['mer'];?>
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
