
$('#category').on('change',function(){
    var id  = $(this).val();
    $('.opt').hide();
    $('.'+id).show();
    $("#caracteristique").val($("#caracteristique option:first").val());
    getResult();
});
$('#category').val($("#category option:first").val());


//Une fois qu'on clique sur le bouton recherche, on appelle la fonction getResult
$('#filterForm').on('submit',function(e){ 
    e.preventDefault(); // permet de bloquer de rafraichir la page
    getResult(e);
});
// keydown, keyup, keypress
$('#nom').on('keyup',function(e){ getResult() }); //Une fois qu'on tappe le nom , on fait appel à la fonction getResult
$('#type').on('change',function(e){ getResult() }); //Une fois qu'on change de type, on fait appel à getResult
$('#caracteristique').on('change',function(e){ getResult() });//Une fois qu'on change de caractéristique, on fait appel à getResult

function getResult(){
    $.ajax({
        method:'post',
        url:$('#filterForm').attr('action'),//il permet de définir le lien à partir de l'attribut action de <form>  , dans notre cas c'est TIDAL-TP/filter
        data : $('#filterForm').serialize()// permet d'envoyer les paramètres (nom, type et caractéristique)  qui l'envoie au Controller
    }).done(function(result){// récuperer les résultats de paramètres envoyés
        $('#result').html(result);//afficher le tableau des résultats
    });
}
getResult();