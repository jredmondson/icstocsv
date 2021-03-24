# icstocsv
A program for converting Google calendars to csv format

# installation
* Download python to your computer (https://www.python.org/downloads/)
  * Install to your path to make calling python easier
* Download the file icstocsv.py to your computer
  * Recommend saving to C:\scripts\icstocsv.py

# grabbing a calendar
* Go to calendar.google.com
* Click on the three dots next to a calendar and select "Settings and Sharing"
* Select "Export Calendar" and save the ics file somewhere (recommend C:\calendars\*)

# convert the calendar to a csv file
* Get to a command prompt (e.g., Start->cmd on Windows)
* Run the icstocsv.py script with the input file and a target csv file to save to

```
python \scripts\icstocsv.py \calendars\mycal.ics \calendars\mycal.csv
```

