import vobject
import csv
import sys
import io

csv_filename = "calendar.csv"

if len(sys.argv) == 1:
  print(f"icstocsv usage: icstocsv [ical file] [csv output file]")
  quit()

if len(sys.argv) > 1:    
  ics_filename = sys.argv[1]
  
  if len(sys.argv) > 2:
    csv_filename = sys.argv[2]

with open(csv_filename, mode='w', encoding="utf-8") as csv_out:
  csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  csv_writer.writerow(['WHAT', 'WHO', 'FROM', 'TO', 'DESCRIPTION'])

  # read the data from the file
  #data = open(ics_filename).read()
  data = io.open(ics_filename, mode="r", encoding="utf-8").read()

  # iterate through the contents
  for cal in vobject.readComponents(data):
    for component in cal.components():
      if component.name == "VEVENT":

        row = ["", "", "", "", ""]
        
        if hasattr(component, 'summary'):
        #if "summary" in component:
          row[0] = component.summary.valueRepr();
          
        
        if hasattr(component, 'attendee'):
        #if "attendee" in component:
          row[1] = component.attendee.valueRepr()
      
        
        if hasattr(component, 'dtstart'):
        #if "dtstart" in component:
          row[2] = component.dtstart.valueRepr()
      
        
        if hasattr(component, 'dtend'):
        #if "dtend" in component:
          row[3] = component.dtend.valueRepr()
      
 
        if hasattr(component, 'description'):
        #if "description" in component:
          row[4] = component.description.valueRepr()
      
        # write to csv
        csv_writer.writerow(row)
