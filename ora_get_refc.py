import oracledb # type: ignore
#con = oracledb.connect('test/test@//localhost:1521/XEPDB1')  

un = 'test'
cs = 'localhost:1521/xepdb1'
pw =  'test'  
con = oracledb.connect(user=un, password=pw, dsn=cs)
dbObjType = con.gettype("TY_VARCHAR_LIST") 
pyobj = dbObjType.newobject()
cur = con.cursor()
refcur = con.cursor()
cur.callproc("get_emp_list_as_refcur", (10,refcur))
print("Printing the values from REFCURSOR:")
for row in refcur:
    #print(row)
    print(row[0])
#print(refcur[1])
#print(refcur[2])
cur.close()  # Close the Cursor
con.close()  # Close the Connection