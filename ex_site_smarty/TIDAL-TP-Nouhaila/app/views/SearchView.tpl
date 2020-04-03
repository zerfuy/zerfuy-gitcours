{include file='header.tpl'}

<div class="container">
    <h2>Recherche Par mot clé</h2>

    <div class="form">
        <input name="nom" value="" id="keyword" placeholder="Le mot clé">
        <button id="submit" type="submit">Recherche</button>
    </div>

    <div id="result" class="search">
      {include file='SearchResult.tpl'}
    </div>
</div>
<script src="{$project_path}/public/js/search.js"></script>
{include file='footer.tpl'}