import pyodbc
class skeema:
    # To initialize connection string to connect database
    # To create cursor object to execute sql commands
    def __init__(self):
        # In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-57\SQLEXPRESS;DATABASE=chandu;UID=admin;PWD=Achandu1@')
        self.cursor = self.cnxn.cursor()
    def create_table(self):
        quairy='''  CREATE TABLE employee_table1 ( emp_id int NOT NULL,
                                                 name varchar(50) NOT NULL,
                                                 salary int NOT NULL,
                                                 project varchar(50) NOT NULL,
                                                  PRIMARY KEY (emp_id));  '''
        self.cursor.execute(quairy)
        self.cnxn.commit()
obj=skeema()
obj.create_table()