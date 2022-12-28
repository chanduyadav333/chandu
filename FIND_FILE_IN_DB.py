import pyodbc
class DB_class_To_store_files:
#To initialize connection string to connect database
#To create cursor object to execute sql commands
    def __init__(self):
        #In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-57\SQLEXPRESS;DATABASE=chandu;UID=admin;PWD=Achandu1@')
        self.cursor = self.cnxn.cursor()
    #To display the contents of the tables from the Database
    def show_file_search_results_fromdb(self):
        values = self.cursor.execute('select * from FileSearchResults_table1')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_location))

   #If the file is not found in the database,found in the drive then it inserted into the database table
    def insert_file_results_into_db(self,fileName, fileLocation, searchCount):
        #sql query for inserting the data into the table
        query = '''  
                    INSERT INTO FileSearchResults_table1 (File_location, searchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        self.cursor.execute(insertQuery)
        self.cnxn.commit()
        print("New file search results committed to DB")

    # to search whether the file is present in database or not

    def search_in_db_for_file(self, fileName):
        # sql query for search the file in database
        query = ''' select * from FileSearchResults_table1 where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = self.cursor.execute(searchQuery)
        print("File search results from DB.")
        flag=1

        for fileInfo in values:

            print("File name: {} - File path: {} ".format(fileInfo.NameOfFile, fileInfo.File_location))
            flag=0

        if flag == 0:
            self.update_file_searchcount(fileName)
            return False
        else:
            return True


    # To update search file count if the file name is already there in the database
    def update_file_searchcount(self, fileName):
        try:
            # sql query for search the data by name
            query = ''' select * from FileSearchResults_table1 where NameOfFile = '{0}' '''
            searchQuery = query.format(fileName)
            values = self.cursor.execute(searchQuery)
            for fileInfo in values:
                fileSearchCount = fileInfo.searchCount
                # To update the search count by incrementing to 1
                fileinfoQuery = '''
                        Update FileSearchResults_table1 SET searchCount = {0} WHERE NameOfFile = '{1}'
                        '''
                updateQuery = fileinfoQuery.format(fileSearchCount + 1, fileName)
                self.cursor.execute(updateQuery)
                # commits data to DB
                self.cursor.commit()
                print("Updated file search count")
        except:
            pass