import os, time

path = r"C:/Users/aryan/Documents/whitehatjr/Python/Project99/testFiles"
now = time.time()
thirtyDaysAgo = now - 30 * 86400

for filename in os.listdir(path):  
    print("This is inside for loop-"+filename)
    fileModTime = os.stat(os.path.join(path, filename)).st_mtime
    print(fileModTime)
    print(thirtyDaysAgo)
    if fileModTime < thirtyDaysAgo:
        print("inside first if")
        if os.path.isfile(os.path.join(path, filename)):
            print("deleting file name-"+filename)
            os.remove(os.path.join(path, filename))
