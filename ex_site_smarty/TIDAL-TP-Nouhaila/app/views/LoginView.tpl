{include file='header.tpl'}
<div class="container">
    <form class="form login" action="{$project_path}/login" method="post">
        <h3 class="form-title">Connexion</h3>
        <input name="login" value="" placeholder="Login">
        <input name="pass" value="" placeholder="Mot de passe">
        <button id="submit" type="submit">Se connecter</button>
        {if isset($error)}
        <small class="error">{$error}</small>
        {/if}
    </form>
</div>
{include file='footer.tpl'}