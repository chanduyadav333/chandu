
import dbcls
import os
import re
import win32api
import threading
import concurrent.futures
class file_search_project:
    def __init__(self):
        self.dbobj=dbcls.dbclsc()
    def find_file(self,root_folder, rex):
        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                print(result)
                if result:
                    file_search_project().insert_file_search_results(root, f, 0)
                    break  # if you want to find only one

    def find_file_in_all_drives(self, file_name):
        # create a regular expression for the file
        rex = re.compile(file_name)
        drives = [drivestr for drivestr in  win32api.GetLogicalDriveStrings().split('\000')[:-1]]
        print(drives)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(self.find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]
            
    def insert_file_search_results(self,fileLocation, fileName, searchCount=0):
        self.dbobj.upload_file_results_todb(fileName, fileLocation, searchCount)

    def search_forfile_indb(self,fileName):
        fileSearchStatus =self.dbobj.search_in_db_for_file(fileName)

        if (fileSearchStatus):
            file_search_project().find_file_in_all_drives(fileName)



o=file_search_project()
o.search_forfile_indb('teja')