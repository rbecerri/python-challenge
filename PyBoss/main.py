import os
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

def getFirstName(fullname):
    return fullname[:fullname.find(" ")]

def getLastName(fullname):
    return fullname[fullname.find(" ")+1:]

def getDOB(dateDOB):
    return str(datetime.strptime(dateDOB, "%Y-%m-%d").strftime("%m/%d/%Y"))

file_path = os.path.join('employee_data.csv')
emps = []
firstNames = []
lastNames = []
dob = []
ssn = []
state = []

with open(file_path) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)
    for row in reader:
        emps.append(row[0])
        firstNames.append(getFirstName(row[1]))
        lastNames.append(getLastName(row[1]))
        dob.append(getDOB(row[2]))
        ssn.append("***-**-{0}".format(row[3][-4:]))
        state.append(us_state_abbrev[row[4]])

newRecords = zip(emps,firstNames, lastNames, dob, ssn, state)
#[print(row) for row in newRecords]

output_file = os.path.join("new_employee_data.csv")
with open(output_file, 'w', newline='') as myFile:
    writer = csv.writer(myFile)
    writer.writerow(["Emp ID","First Name","Last Name","DOB,SSN","State"])
    writer.writerows(newRecords)
