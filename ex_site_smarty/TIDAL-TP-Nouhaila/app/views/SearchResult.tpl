<table>
    {if !empty($pathologies)}<!--si le résultat n'est pas vide -->
    <tr>
        <th>Id Pathologie</th><th>Méridien</th><th>Type</th><th>Description</th>
    </tr>
        {foreach from=$pathologies item=$patho}
        <tr>
            <td>{$patho.idP}</td>
            <td>{$patho.mer}</td>
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