import getpass

import oracledb

un = 'test'
cs = 'localhost:1521/xepdb1'
pw =  'test'    #getpass.getpass(f'Enter password for {un}@{cs}: ')

print(cs)
print(un)
with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
    with connection.cursor() as cursor:
        sql = """select ename ,sal from emp"""
        for r in cursor.execute(sql):
           #print(r)
            print(r[0])
            print(r[1])
            