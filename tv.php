<?php

$tags = 'power,input,mute,1,2,3,4,5,6,7,8,9,0,vol+,vol-,ch+,ch-,soccer,settings,up,info,left,enter,right,back,down,exit,red,green,yellow,blue';
$tagsArray = explode(",", $tags);

$nome = $_POST['name'];

$count = 0;

foreach ($tagsArray as $tag) {
	if ($tag == $nome) {
		$count++;
	}
}

if ($count > 0) {	
	echo json_encode("sudo irsend SEND_ONCE tv_lg key_$nome");
	shell_exec("sudo irsend SEND_ONCE tv_lg key_$nome");
}else{
	echo json_encode("Não encontrada");
}

?>
