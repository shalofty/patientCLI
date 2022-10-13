# CLI for ADT data
# Below are several quick implimentations of functions for interacting with adt data in a csv file
#imports
import pandas as pd
import csv

# Arrays of fields for comparison operations
hospital = ["Meritus Medical Center", "Sinai Hospital", "Johns Hopkins", "Luminis Health", "University of Maryland Medical Center"]
event = ["Discharge", "Admit"]
care = ["Emergency", "Inpatient"]

# read csv with pandas
data = pd.read_csv("EncounterNotificationSampleData.csv")

# creating lists from columns
eventID = data['EventID'].tolist()
patientID = data['PatientID'].tolist()
hospitalName = data['HospitalName'].tolist()
eventDate = data['EventDate'].tolist()
eventType = data['EventType'].tolist()
careLevel = data['LevelOfCare'].tolist()
chiefComplaint = data['Chief Complaint'].tolist()

# Array of column names for csv file to act as parameter for findEmpty function
columns = [eventID, patientID, hospitalName, eventDate, eventType, careLevel, chiefComplaint]

# pdPrint functions, prints all columns
def pdPrint():
    # print(data.to_string())
    print(data[["HospitalName", "PatientID", "EventDate", "EventType", "LevelOfCare", "Chief Complaint"]].to_string())

# findEmpty function, finding nan fields in csv file
def findEmpty(columns):
    # Creating lists for each column
    # Each list has 45 items, blank fields output 'nan'
    print("Which field would you like to search for blanks?")
    print("""
    Enter a number
    1) Patient ID
    2) Hospital name
    3) Date
    4) Event type (Discharge/Admit)
    5) Level of Care
    6) Chief Complaint 
    """)
    emptyChoice = int(input(">>>"))
    blanks = 0
    for field in columns[emptyChoice]:
        # pd.isna is panda function to determine is value is not a nan
        if pd.isna(field) == True:
            blanks += 1
    blanks = str(blanks)
    print("There are " + blanks + " blank fields in the column.")
    print(columns[emptyChoice])

# printAll function
def printAll():
    # Open csv file
    with open('EncounterNotificationSampleData.csv', 'r') as ENSD:
        file = csv.reader(ENSD)
        # iterate through columns
        for col in file:
            print(col[1] + "\t" + col[4] + "\t" + col[5] + "\t\t" + col[2])

# findPatient function
def findPatient():
    # Open csv file
    print("Enter patient ID: ")
    searchPID = input(">>>")
    with open('EncounterNotificationSampleData.csv', 'r') as ENSD:
        file = csv.reader(ENSD)
        # iterate through columns
        for col in file:
            for field in col:
                if searchPID == field:
                    print("##############################################################################")
                    print("PATIENT ADT CARD")
                    print("EVENT ID: "+ col[0] + "\t PATIENT ID: " + col[1] + "\t VISIT DATE: " + col[3])
                    print("HOSPITAL: " + col[2] + "\t CHIEF COMPLAINT: " + col[6])
                    print("LEVEL OF CARE: " + col[5] + "\t EVENT TYPE: " + col[4])
                    break

# byHospital function
def byHospital():
    # Open csv file
    print("Search by hospital: ")
    print(hospital)
    searchHospital = input(">>>")
    with open('EncounterNotificationSampleData.csv', 'r') as ENSD:
        file = csv.reader(ENSD)
        # iterate through columns
        for col in file:
            for field in col:
                if searchHospital == field:
                    print(col[1] + "\t" + col[2])
                    break

    print("Select a patient? (y/n)")
    selectP = input(">>>").upper()
    if selectP == "Y":
        findPatient()

# findDuplicates function
def findDuplicates():
    boolean = not data["PatientID"].is_unique
    boolean = data["PatientID"].duplicated().any()
    if boolean == True:
        print("There are duplicate Patient ID's.")
    elif boolean != True:
        print("There aren't any duplicate entries.")

# User Menu
prompt = 0
while prompt < 1:
    print("Hospital Encounter Search Console")
    print("""
    1) Print All
    2) Find patient by ID
    3) All patients in hospital
    4) Incomplete patient profiles
    5) Find duplicates
    0) Exit
    """)
    menuSelect = input(">>>")
    if menuSelect == "1":
        pdPrint()
    elif menuSelect == "2":
        findPatient()
    elif menuSelect == "3":
        byHospital()
    elif menuSelect == "4":
        findEmpty(columns)
    elif menuSelect == "5":
        findDuplicates()
    elif menuSelect == "0":
        prompt += 1