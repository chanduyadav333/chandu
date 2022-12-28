import os
import re
import win32api
import FIND_FILE_IN_DB
import concurrent.futures

#this class is to perform operations on drives to search the files in drives
class Find_FileLocation_In_Drives:
#this constuctor is initialize the DB_class_To_store_files class object
    def __init__(self):
        self.uploadObject = FIND_FILE_IN_DB.DB_class_To_store_files()

    # this method is take two arguments as inputs drive and file name
    #if the file is found in drives it calls the insert_file_search_results method
    def find_file(self, root_folder, rex):
        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    print("File name: {} - File location: {}".format(f, root))
                    # call to method insert_file_search_results to upload file search results to db
                    self.insert_file_search_results(root, f, 0)
                    break  # if you want to find only one

    # Method find_file_in_all_drives is used to get all the available drives in our local system/VM
    def find_file_in_all_drives(self, file_name):
        # create a regular expression for the file
        rex = re.compile(file_name)

        drives = [drivestr for drivestr in  win32api.GetLogicalDriveStrings().split('\000')[:-1]]
        print(drives)
        #multi-threading by using concurrency futures
        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(self.find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]

    #by calling this method insert data into the database table
    def insert_file_search_results(self, fileLocation, fileName, searchCount):
        self.uploadObject.insert_file_results_into_db(fileName, fileLocation, searchCount)

    #this method first call search_in_db_for_file method from DB_class_To_store_files
    #if the file already searched then searchcount is increment by one
    # else find_file_in_all_drives method is call
    def search_forfile_indb(self, fileName):
        fileisnotfountindb=self.uploadObject.search_in_db_for_file(fileName)
        print("File search results from local drive")
        if fileisnotfountindb:
            self.find_file_in_all_drives(fileName)



locationObject = Find_FileLocation_In_Drives()
fileToSearch = input()
locationObject.search_forfile_indb(fileToSearch)