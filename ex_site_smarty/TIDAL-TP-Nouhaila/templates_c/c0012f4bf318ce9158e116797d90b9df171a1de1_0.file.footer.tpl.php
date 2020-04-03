<?php
/* Smarty version 3.1.33, created on 2019-10-06 14:56:04
  from 'C:\wamp64\www\tlial_tt\TLIAL_projet_1\TIDAL-TP-Nouhaila\app\views\footer.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.33',
  'unifunc' => 'content_5d9a00846574f0_75741237',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'c0012f4bf318ce9158e116797d90b9df171a1de1' => 
    array (
      0 => 'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\app\\views\\footer.tpl',
      1 => 1570373702,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5d9a00846574f0_75741237 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_checkPlugins(array(0=>array('file'=>'C:\\wamp64\\www\\tlial_tt\\TLIAL_projet_1\\TIDAL-TP-Nouhaila\\vendor\\smarty\\smarty\\libs\\plugins\\modifier.date_format.php','function'=>'smarty_modifier_date_format',),));
?>




<p class="footer-menu">

<a target="_blank" href='<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/output'>PhpDocumentor</a> |
<a target="_blank" href='<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/webservices/WS-simple/calculatrice/addition/1/2'>Web Services caculatrice</a> |
<a target="_blank" href='<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/webservices/WS-xml'>Web Services XML</a> |

</p>


<p class="copyright">Copyright &copy; <?php echo smarty_modifier_date_format(time(),"%Y");?>
 | Designed by nouhaila</p>

<?php echo '<script'; ?>
 src="<?php echo $_smarty_tpl->tpl_vars['project_path']->value;?>
/public/js/main.js"><?php echo '</script'; ?>
>
</body>
</html><?php }
}
