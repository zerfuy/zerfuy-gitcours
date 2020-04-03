{include file='header.tpl'}
<div class="container">
    <form class="form" action="{$project_path}/register" method="post">
        <h3 class="form-title">Inscription</h3>
        <table style="max-width:400px">
            <tr>
                <td>
                    <label>Prénom</label>
                </td>
                <td>
                    <input name="fname" value="{$form.fname}" placeholder="Prénom" required>
                </td>
            <tr>
            <tr>
                <td>
                    <label>Nom</label>
                </td>
                <td>
                    <input name="lname" value="{$form.lname}" placeholder="Nom" required>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Login</label>
                </td>
                <td>
                    <input name="login" value="{$form.login}" placeholder="Login" required>
                </td>
            </tr>
            <tr>
                <td>
                    <label>Mot de passe</label>
                </td>
                <td>
                    <input name="pass" type="password" value="{$form.pass}" placeholder="Mot de passe" required>
                </td>
            </tr>
            <tr>
                <td colspan="2">
                    <button id="submit" type="submit">S'inscrire</button>
                </td> 
            </tr> 
        </table> 
        {if isset($error)}
        <small class="error">{$error}</small>
        <small class="info">Veuillez saisir obligatoirement le nom, prénom, login sous forme de caractère entre a et z.</small>
        {/if} 
    </form> 
</div> 
{include file='footer.tpl' }