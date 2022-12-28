import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-57\SQLEXPRESS;DATABASE=chandu;UID=admin;PWD=Achandu1@')
cursor=conn.cursor()
cursor.execute('''INSERT INTO FileSearchResults_table1 (File_Location,searchCount,NameOfFile) VALUES ('C:\chandu\ProgrammingDemo.txt',1,'ProgrammingDemo.txt')''')
conn.commit()