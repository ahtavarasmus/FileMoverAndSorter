import os
import time
import datetime
import threading
from pathlib import Path
import shutil


def movingTheFile(start, end):

    for posNum in range(start, end + 1):
        og_path = filenamelist[posNum]
        # getting the last modified time as a datetime:
        # mtime = 1585501464.0
        mtime = os.path.getmtime(og_path)
        date = time.ctime(mtime)  # date = Sun Mar 29 20:04:24 2020'

        # getting the datetime object
        # datetime.datetime(2020, 3, 29, 20, 4, 24)
        datetimeObj = datetime.datetime.strptime(date, '%a %b %d %H:%M:%S %Y')

        # Getting a year from datetimeObj
        year = datetimeObj.year  # year = 2020
        month = datetimeObj.strftime('%B')  # month = march

        filename = os.path.basename(og_path)
        newPath = 'D:\\sortedtest1\\{}\\{}'.format(year, month)

        Path(newPath).mkdir(parents=True, exist_ok=True)  # windowsPath object

        newfilePath = os.path.join(newPath, filename)
        print('Copying {} to {}'.format(full_path, newfilePath))
        shutil.copy(full_path, newfilePath)


filenamelist = []  # list of all the filenames in a drive
for foldername, subfolders, filenames in os.walk('C:\\Users\\ahtav\\Videos\\Desktop'):
    for filename in filenames:
        full_path = os.path.join(foldername, filename)
        filenamelist.append(full_path)
# Create and start the Thread objects.
downloadThreads = []
listLen = len(filenamelist)
for i in range(0, listLen + 1, 10):
    start = i
    if (listLen - i) < 10:
        end = i + (listLen-i)
        movingTheFile(start, end)
    else:
        end = i + 9
    downloadThread = threading.Thread(target=movingTheFile, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
