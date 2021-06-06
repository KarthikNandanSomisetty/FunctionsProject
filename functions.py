import os
import shutil
import time

path = input("enter the path of folder to delete it: ")
days = 59
seconds=time.time() - (days*2*60*60)
path = path + "/"

list_of_files = os.listdir(path)

def file_time(path):
	ctime = os.stat(path).st_ctime
	return time


if os.path.exists(path):
    for file in list_of_files:
        if seconds >= file_time(path):
            os.remove(path + file)
            print("files deleted")

        else:
            print("the file choosen exists less than 59 days.enter the file path that exists more than 59 days.")
        elif:
            print("the entered path does not exist")