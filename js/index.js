function processForm(){

    var data = new FormData($("#form")[0]);

    $.ajax( {
               type: 'POST',
               url: 'recebe.php',
               dataType: 'json',
               cache: false,
               processData: false,
               contentType: false,
               timeout: 8000,
               data: data,

               success: function(result) {
                   $('#resposta').html(result);
               }
           } );

}
