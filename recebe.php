<?php

    if (isset($_POST['aceso'])) {
		system("sudo python scripts/led.py 2 1");
        echo json_encode("Está aceso");
    } else {
		system("sudo python scripts/led.py 2 0");
        echo json_encode("Está apagado");

    }

?>
