<?php
$servername = "localhost";
$username = "root";
$password = "root";

// Create connection
$conn = new mysqli($servername, $username, $password,"embeddedpi");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

//$query = "insert into valores (hora,valor) values ('16:22','30')";

//if(mysqli_query($conn,$query) === TRUE){
//	echo "Inseriu";
//}else{
//	echo "Erro ao adicionar!!!";
//}

$query = sprintf("select hora,valor from valores order by id;");

//delete from sensor.valores where id=5;
//SELECT COUNT(*) FROM table_name;

$result = mysqli_query($conn,$query);

$data = array();
foreach ($result as $row) {
	$data[] = $row;
}

echo json_encode($data);

mysqli_close($conn);



//echo "Connected successfully";
?>
