
$('#keyword').on('keyup',function(){
    value = $(this).val();
    search(value);
});
$('#submit').on('click',function(){
    value = $("#keyword").val();
    search(value);
});




function search(keyword){
    $.ajax({
        method:'POST',
        data:"keyword=" + keyword,
        url:"search"
    }).done(function(result){
        $("#result").html(result);
    });
}