#this class is used to create new table
class schema:
    # To initialize connection string to connect database
    # To create cursor object to execute sql commands
    def __init__(self):
        # In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-57\SQLEXPRESS;DATABASE=chandu;UID=admin;PWD=Achandu1@')
        self.cursor = self.cnxn.cursor()
    #this method create new table by using connection string, cnxn,cursor objects
    def create_table(self):
        #query for create new table with primary key column
        query='''  CREATE TABLE employee_table1 ( emp_id int NOT NULL,
                                                 name varchar(50) NOT NULL,
                                                 salary int NOT NULL,
                                                 project varchar(50) NOT NULL,
                                                  PRIMARY KEY (emp_id));  '''
        self.cursor.execute(query)
        self.cnxn.commit()

#user defind exception
#if project name not in list it's throw exception
class insertexception(Exception):
    def __str__(self):
        return "projent name not in list of the projects"
#user defind exception
#if id alredy exists in table it's throw exception
class id_exception(Exception):
    def __str__(self):
        return "id already exist enter new id for employee"
#user defind exception
#if bonus limit not in between 0 t0 200% it's throw exception
class bonus_ex(Exception):
    def __str__(self):
        return "bonus is very high enter with in range"
import pyodbc
class EMPLOYEE:
    def __init__(self):
        #In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-57\SQLEXPRESS;DATABASE=chandu;UID=admin;PWD=Achandu1@')
        self.cursor = self.cnxn.cursor()
        self.project=['c','java','python']
    #this method is used to insert new employee details in database table
    def add_employee_details(self,id,name,salary,project):
        #query get id if the egument id in table
        query_for_search_id=''' select emp_id from employee_table1  '''.format(id)
        value_of_query_for_search_id=self.cursor.execute(query_for_search_id)
        #indication for id already exists or not
        f=False
        for i in value_of_query_for_search_id:
            if i.emp_id == id:
                f=True
                break
        #check if id alredy in table it will throw exception
        if f:
            try:
                raise id_exception
            except id_exception as id_ex:
                print(id_ex)
        #id not exist in table it will insert the details in table
        else:
            #query to insert
            insertquery = '''  INSERT INTO employee_table1 (emp_id,name,salary,project) values ({0},'{1}',{2},'{3}') '''.format(id, name, salary, project)
            #if the project is in list it insert in table
            if project in self.project:
                self.cursor.execute(insertquery)
                self.cnxn.commit()
                print("details insert successfully in db")
            #if tha project is not in list it will throw exception
            else:
                try:
                    raise insertexception
                except insertexception as ex:
                    print(ex)
    #to update the project or salary and both
    def update_details(self,id,project='',salary=0):
        #if salary argument is given it will upadte otherwise not
        if salary !=0:
            #query for update
            insertquery_for_salary_update= ''' UPDATE employee_table1 SET salary = {0} where emp_id = {1} '''.format(salary,id)
            self.cursor.execute(insertquery_for_salary_update)
            self.cnxn.commit()
            print("updated successfully")
        #if project argument is geven it will update ohetwise not
        if project:
            # query for update
            insertquery_for_project_update= ''' UPDATE employee_table1 SET project = '{0}' where emp_id = {1} '''.format(project, id)
            self.cursor.execute(insertquery_for_project_update)
            self.cnxn.commit()
            print("updated successfully")
    #To display all employeee details in table
    def display_employee_details(self):
        query_for_display_details='''select * from employee_table1 '''
        values=self.cursor.execute(query_for_display_details)
        for i in values:
            print("employee id ",i.emp_id," employee name ",i.name," salary ",i.salary," project ",i.project)
    #To delete particular employee details
    def delet_employee_details(self,id):
        #delet query
        query=''' DELETE from employee_table1 where emp_id = {0}   '''.format(id)
        self.cursor.execute(query)
        self.cnxn.commit()
        print("deleted successfully")
    #To add bonus and salary inster into salary column
    def add_bonus(self,id,bonus):
        #if bonus is in between 0 to 200% then it will insert otherwise it will throw exception
        if bonus > 0 and bonus <= 2:
            #To get salary from table
            query = ''' select salary from employee_table1 where emp_id = {}'''.format(id)
            value = self.cursor.execute(query)
            for i in value:
                salary = i.salary
            new_salary = salary + salary * bonus
            #To update salary by adding bonus
            query_for_update_bonus = ''' UPDATE employee_table1 SET salary = {0} where emp_id = {1} '''.format(new_salary, id)
            self.cursor.execute(query_for_update_bonus)
            self.cnxn.commit()
            print("bouns updated successfully")
        #if the bonus exeds limit it will throw exception
        else:
            try:
                raise bonus_ex
            except bonus_ex as ex:
                print(ex)
#to cretate object for EMPLOYEE class
#obj=EMPLOYEE()
#to add new employee details
#obj.add_employee_details(4,'rakesh',100000,'c')
#if to update only salry
#obj.update_details(1,'',200000)
#if to update only project
#obj.update_details(1,'python',)
#to update both
#obj.update_details(2,'java',70000)
#to display all employee details
#obj.display_employee_details()
#to delete particular employee details
#obj.delet_employee_details(1)
#to add bonus
#obj.add_bonus(2,1)
