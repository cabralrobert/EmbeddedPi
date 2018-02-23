$(document).ready(function(){

	$.ajax({
		url: "../umidade.php",
		type: "GET",
		contentType: "application/json; charset=utf-8",
		success: function(data){
			data = JSON.parse(data);
			console.log(data);

			var valores = {
				hora : [],
				valor : []				
			};

			var len = data.length;

			for(var i = 0; i < len; i++){
				valores.hora.push(data[i].hora);
				valores.valor.push(data[i].valor);
			}

			console.log(valores);

			var ctx = document.getElementById("lineumidade").getContext('2d');

			var dadosgraph = {
				labels : valores.hora,
				datasets: [
					{
						label: "teste",
						data : valores.valor,						
				  		fillColor : "rgba(151,187,205,0.5)",
				          strokeColor : "rgba(151,187,205,1)",
				          pointColor : "rgba(151,187,205,1)",
				          pointStrokeColor : "#fff",			  		

					}
				]
			};

			new Chart(document.getElementById("lineumidade").getContext('2d')).Line(dadosgraph);			  


		},
		error : function(data){
			console.log(data);
		}

	});

});
