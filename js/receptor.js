function teste(quem){

    var data = $(quem).attr('id');

    $.ajax( {
               method: 'POST',
               url: 'receptor.php',
               dataType: 'json',
               data: {name:data},

               success: function(result) {
                   console.log(result);
               },
               error: function(result){
                   console.log(result);
               }
           });

}
