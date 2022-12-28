import os
import concurrent.futures
import time
import win32api
start=time.perf_counter()
availableDrive=win32api.GetLogicalDriveStrings()
Drives=[drivestr for drivestr in availableDrive.split('\000') if drivestr]

def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
input_file='ProgrammingDemo.txt'
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(find_files,input_file,drive) for drive in Drives]
    for r in concurrent.futures.as_completed(results):
        print(r.result())
finish=time.perf_counter()
print(f"time {finish-start} seconds")