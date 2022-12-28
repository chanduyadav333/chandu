import win32api

print(avd)
drives=[drivestr for drivestr in avd.split('\000') if drivestr]
print(drives)