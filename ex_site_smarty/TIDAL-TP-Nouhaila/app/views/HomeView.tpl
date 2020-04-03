{include file='header.tpl'}
<div class="container">
    <h2>TIDAL TP PROJECT</h2>
<div class="cover">
{if !isset($smarty.session.TIDAL_USER_ID)}
    {* Si l'utilisateur n'est pas connecté *}
    <form class="form login" action="{$project_path}/login" method="post">
        <h3 class="form-title">Connexion</h3>
        <input name="login" value="" placeholder="Login">
        <input name="pass" value="" placeholder="Mot de passe">
        <button id="submit" type="submit">Se connecter</button>
    </form>
{/if}
</div>

<div class="cards">
    <div class="card">
        <h4>Liste des méridiens</h4>
        <ul>
            {* Afficher le nom de chaque méridien (foreach) *}
            {foreach from=$rss.meridiens item=mer}
            <li>{$mer.nom}</li>
            {/foreach}
        </ul>
    </div>

    <div class="card">
        <h4>Liste des pathologies</h4>
        <ul>
            {foreach from=$rss.pathos item=patho}
            <li>{$patho.desc}</li>
            {/foreach}
        </ul>
    </div>

    <div class="card">
        <h4>Liste des symptômes</h4>
        <ul>
            {foreach from=$rss.symptomes item=sym}
            <li>{$sym.desc}</li>
            {/foreach}
        </ul>
    </div>
</div>


</div>
{include file='footer.tpl'}