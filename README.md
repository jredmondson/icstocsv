# icstocsv
A program for converting Google calendars to csv format

# installation
* Download python to your computer (https://www.python.org/downloads/)
  * Install to your path to make calling python easier
  * Install vobject module via pip
* Download git to your computer (https://tortoisegit.org/download/)
  * TortoiseGit is a visual interface on your Windows Explorer which may be easier to use for people uncomfortable on the Windows command line
  * Git for Windows is more of a command line interface for power users (https://git-scm.com/download/win)
  * TortoiseGit will allow you to also install Git for Windows (and this is recommended)
```
pip install vobject
```
* Download the file icstocsv.py to your computer
  * Recommend saving to /scripts/icstocsv.py

# grabbing this code base
* Use git to download this repository
* It is recommended to save this code in \code\icstocsv or a similar structure that is easy for you to reference from a command line
* In TortoiseGit, it is recommended that you save the repo at \code\icstocsv and not the default of \code\icstocsv\icstocsv

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
icstocsv usage: icstocsv ical [csv output file]

  if no csv out provided, then saves at ical.csv
```
