import oracledb # type: ignore

#con = oracledb.connect('test/test@//localhost:1521/XEPDB1')  

un = 'test'
cs = 'localhost:1521/xepdb1'
pw =  'test'  
con = oracledb.connect(user=un, password=pw, dsn=cs)
print("Database version:", con.version)
if con.is_healthy():
    print("Healthy connection!")
else:
    print("Unusable connection. Please check the database and network settings.")
dbObjType = con.gettype("TY_VARCHAR_LIST") 
pyobj = dbObjType.newobject()
cur = con.cursor()   # connection cursor 
cur.callproc("get_emp_list_as_coll", (10,pyobj,)) # Call the Procedure
cur.close() # Close the Cursor
con.close() # Close the Connection
print("Printing the values of collection as list:")
print(pyobj.aslist())