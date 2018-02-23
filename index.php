<?php

define('DB_SERVER','localhost');
define('DB_USERNAME','postgres');
define('DB_PASSWORD','');
define('DB_NAME','sensor');

$link = pg_connect("host=localhost dbname=sensor user=root password=root");
if (!$link) {
    die('Não foi possível conectar:');
}
//echo 'Conexão bem sucedida<br>';

$result = pg_query($link,"select hora,valor from valores order by id;");

if(!$result){
	echo "Não executou";	
}

$data = array();

if(pg_num_rows($result) == 0){
	echo "nenhum valor";
}else{
	while($row = pg_fetch_array($result)){
		unset($row[0]);
		unset($row[1]);
		$data[] = $row;
	}
}
	


echo json_encode($data);
pg_close($link);

/*$query = "insert into valores (hora,valor) values ('16:22','30')";

if(mysqli_query($link,$query) === TRUE){
	echo "Inseriu";
}else{
	echo "Erro ao adicionar!!!";
}

$query = sprintf("select hora,valor from valores order by id;");

//delete from sensor.valores where id=5;
//SELECT COUNT(*) FROM table_name;

$result = mysqli_query($link,$query);

$data = array();
foreach ($result as $row) {
	$data[] = $row;
}

echo json_encode($data);

mysqli_close($link);
*/
?>
