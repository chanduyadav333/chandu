'''import re
import win32api
import os
import time
s=time.perf_counter()
class file_project:
    def find_file(self,root_folder, rex):
        l =[]
        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    l.append(os.path.join(root, f))
        return l

                     # if you want to find only one

    def find_file_in_all_drives(self,file_name):
        # create a regular expression for the file
        rex = re.compile(file_name)
        l=[]
        for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
           if file_project().find_file(drive, rex):
               l.append(file_project().find_file(drive, rex))
        return l


o=file_project()
print(o.find_file_in_all_drives("ProgrammingDemo.txt"))
rq=time.perf_counter()
print(rq-s)'''
import SoftwareEngineer.Developers.demo_for_packages
SoftwareEngineer.Developers.demo_for_packages.srinu().f()
