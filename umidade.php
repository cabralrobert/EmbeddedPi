<?php
$servername = "localhost";
$username = "root";
$password = "root";

$conn = new mysqli($servername, $username, $password,"embeddedpi");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$query = sprintf("select hora,valor from umidade order by id;");

$result = mysqli_query($conn,$query);

$data = array();
foreach ($result as $row) {
	$data[] = $row;
}

echo json_encode($data);

mysqli_close($conn);

?>

