<?php
$servername = "localhost";
$username = "robertc";
$password = "9346";

$conn = new mysqli($servername, $username, $password,"embeddedpi");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$query = sprintf("select hora,valor from valores order by id;");

$result = mysqli_query($conn,$query);

$data = array();
foreach ($result as $row) {
	$data[] = $row;
}

echo json_encode($data);

mysqli_close($conn);

?>

