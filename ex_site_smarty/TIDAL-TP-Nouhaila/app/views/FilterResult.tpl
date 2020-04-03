<table>
    {if !empty($pathologies)}<!--si le résultat n'est pas vide -->
    <tr>
        <th>Code Méridien</th><th>Nom Méridien</th><th>Type</th><th>Description</th>
    </tr>
        {foreach from=$pathologies item=$patho}
        <tr>
            <td>{$patho.code}</td>
            <td>{$patho.nom}</td>
            <td>{$patho.type}</td>
            <td>{$patho.desc}</td>
        </tr>
        {/foreach}
    {else}
    <tr>
        <td>Aucun resultat trouvé</td>
    </tr>
    {/if}
</table>