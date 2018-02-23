$(document).ready(function(){

	$.ajax({
		url: "../tempatual.php",
		type: "POST",
		contentType: "application/json; charset=utf-8",
		dataType: 'json',
		cache: false,
		processData: false,
		timeout: 8000,
		
		success: function(data){
			$('#tempatual').html(data);
		}
	});

});


