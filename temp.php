<?php

	$retorno = shell_exec("sudo python scripts/dht11.py");
	$valores = explode("|",$retorno);
	$valores[1]=str_replace("\n","",$valores[1]);
	$valores=array('temp' => $valores[0], 'umid' => $valores[1]);
	echo json_encode($valores);

?>
