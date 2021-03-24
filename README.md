# icstocsv
A program for converting Google calendars to csv format

# installation
* Download python to your computer (https://www.python.org/downloads/)
  * Install to your path to make calling python easier
  * Install vobject module via pip
```
pip install vobject
```
* Download the file icstocsv.py to your computer
  * Recommend saving to /scripts/icstocsv.py

# grabbing a calendar
* Go to calendar.google.com
* Click on the three dots next to a calendar and select "Settings and Sharing"
* Select "Export Calendar" and save the ics file somewhere (recommend `/calendars/*`)

# convert the calendar to a csv file
* Get to a command prompt (e.g., Start->cmd on Windows or a terminal in Linux/Mac)
* Run the icstocsv.py script with the input file and a target csv file to save to

```
python \scripts\icstocsv.py \calendars\mycal.ics \calendars\mycal.csv
```

# get usage info
* Call the script with no arguments to get usage
```
python icstocsv.py
icstocsv usage: icstocsv [ical file] [csv output file]
```
