
<?php
echo "Free Proxy</br>";
if (isset($_POST['url']))
{
$link = $_POST['url'];
$filename = './curled/'.rand().'txt';
$curlobj = curl_init($link);
$fp = fopen($filename,"w");
curl_setopt($curlobj, CURLOPT_FILE, $fp);
curl_setopt($curlobj, CURLOPT_HEADER, 0);
curl_setopt($curlobj, CURLOPT_FOLLOWLOCATION, true);
curl_exec($curlobj);
curl_close($curlobj);
fclose($fp);
$fp = fopen($filename,"r");
$result = fread($fp, filesize($filename));
fclose($fp);
echo $result;
}
?>
 <form name="bizLoginForm" method="post" action"" >

    URL:<input type="text" id="url" name="url"/>
    <input type="Submit" value="Browse" />
</form>
<a href="local.php">Developer Access</a>
