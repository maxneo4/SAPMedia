# Phyton virtual environment #

## Installed packages ##

1. pyexcel includes (pyexcel-io)
2. pyexcel-xlsx (xlsx format)
3. flask (rest server framework)


## Templates reports documentation dev
<http://jinja.pocoo.org/docs/dev/templates/>

pysqlite
Microsoft Visual C++ 9.0 is required (Unable to find vcvarsall.bat). Get it from http://aka.ms/vcpython27

```sql
WITH csvrec(l,c,owner, type, year, month) AS (
       SELECT 1,
       owner||',',        
       '',
       type,       
       strftime("%Y" , date) as year,
       strftime("%m", date) as month       
       from publication
     UNION ALL
       SELECT  
              instr(c,',') AS vLen,  
              substr(c,instr(c,',')+1) AS vRem,               
              trim( substr(c,1,instr(c,',')-1) ) AS vCSV ,              
              type, year, month
       FROM csvrec
       WHERE vLen>0
     )      
     select owner,
     count(owner) as number,
     type, year, month
     from csvrec
     where owner is not ''
     group by owner, type, year, month
     order by number DESC
```
