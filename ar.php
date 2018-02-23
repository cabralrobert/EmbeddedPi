<?php

  $temp = $_POST['temp'];
  $velocidade = $_POST['velo'];
  $swing = $_POST['swing'];
  $poweroff = $_POST['poweroff'];

  if ($temp != "0" && $velocidade != "0") {
	shell_exec("sudo irsend SEND_ONCE lg_ac ac_".$velocidade."_".$temp);
    echo json_encode("sudo irsend SEND_ONCE lg_ac ac_".$velocidade."_".$temp);
  }

  if ($temp =="0" && $poweroff == "-1") {    
      if($swing == "true"){
		shell_exec("sudo irsend SEND_ONCE lg_ac swing_on");
        echo json_encode("sudo irsend SEND_ONCE lg_ac swing_on");      
	}
      else{
		shell_exec("sudo irsend SEND_ONCE lg_ac swing_off");
        echo json_encode("sudo irsend SEND_ONCE lg_ac swing_off");      
	}
  }  

  if ($temp =="0" && $swing == "n") {    
      if($poweroff == "on"){
		shell_exec("sudo irsend SEND_ONCE lg_ac ac_on");
        echo json_encode("sudo irsend SEND_ONCE lg_ac ac_on");      
		}
      else{
		shell_exec("sudo irsend SEND_ONCE lg_ac ac_off");
        echo json_encode("sudo irsend SEND_ONCE lg_ac ac_off");      
		}
  }  

?>
