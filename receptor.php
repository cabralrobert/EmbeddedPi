<?php

$tags = 'power,mute,1,2,3,4,5,6,7,8,9,0,tvr,recall,menu,epg,fav,exit,up,left,enter,right,down,sat,red,green,yellow,blue,tvav,zoom,sleep,info,10ch+,10ch-,audio,text,subtitle,play,stop,pause,record';
$tagsArray = explode(",", $tags);

$nome = $_POST['name'];

$count = 0;

foreach ($tagsArray as $tag) {
        if ($tag == $nome) {
                $count++;
        }
}

if ($count > 0) {
        echo json_encode("sudo irsend SEND_ONCE receptor key_$nome");
        shell_exec("sudo irsend SEND_ONCE receptor key_$nome");
}else{
        echo json_encode("Não encontrada");
}

?>
