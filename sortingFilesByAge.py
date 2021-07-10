import os
import time
import datetime
from pathlib import Path
import shutil


def movingTheFile(og_path):

    # getting the last modified time as a datetime:
    # mtime = 1585501464.0
    mtime = os.path.getmtime(og_path)
    date = time.ctime(mtime)  # date = Sun Mar 29 20:04:24 2020'

    # getting the datetime object
    # datetime.datetime(2020, 3, 29, 20, 4, 24)
    datetimeObj = datetime.datetime.strptime(date, '%a %b %d %H:%M:%S %Y')

    # Getting a year from datetimeObj
    year = datetimeObj.year  # year = 2020
    month = datetimeObj.strftime('%B')  # month = 3

    filename = os.path.basename(og_path)
    newPath = 'D:\\sortedtest1\\{}\\{}'.format(year, month)

    Path(newPath).mkdir(parents=True, exist_ok=True)  # makes a directory if it doesn't exist

    newfilePath = os.path.join(newPath, filename)
    print('Copying {} to {}'.format(full_path, newfilePath))
    # uncomment the next line when ready
    # shutil.copy(full_path, newfilePath)



for foldername, subfolders, filenames in os.walk('C:\\Users\\ahtav\\Videos\\Fortnite'):
    for filename in filenames:
        full_path = os.path.join(foldername, filename)
        movingTheFile(full_path)
