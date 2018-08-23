<?php

	$retorno = shell_exec("sudo python scripts/dht11.py");
	$valores = explode("|",$retorno);


	echo json_encode("<li> <h1>Temperatura: $valores[0]</h1></li><li><h1>Umidade: $valores[1]</h1></li>");



?>
