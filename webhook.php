<?php

$json = file_get_contents('php://input');
$request_body = json_decode($json, true);
$sender_id = $request_body['sender_id'];
$message = $request_body['message'];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'http://localhost:5005/webhooks/rest/webhook');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, "{\"sender\": \"$sender_id\", \"message\": \"$message\"}");
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
$response = curl_exec($ch);
curl_close($ch);

echo $response;

?>
