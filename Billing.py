#Billing Software for le'valor lab

from itertools import count
from sqlite3 import Date
from datetime import datetime
from time import time
from weakref import ref

#header Section
bill_no    = int(input("Enter Bill Number     : "))
ref_no     = int(input("Enter Reference Number: "))
now        = datetime.now()
dt_string  = now.strftime("%d/%m/%Y %H:%M:%S")

#Patient Section
date_collection = input("Enter Date of Collection :")
time_collection = input("Enter Time of Collection :")
patient_name    = input("Enter Patient Name       :")
patient_age     = input("Enter Patient Age        :")
patient_gender  = input("Enter Gender of patinet  :")
ref_doctor      = input("Enter Refered Doctor Name:") 
collected_at    = input("Enter Collection Point   :")

#unction print patient & test headers
def patient_det():
        print("""
        ----------------------------------------------------------------------------------------
             Bill No: {}           Reference No: {}            Date & Time: {}
        ----------------------------------------------------------------------------------------

            Date of Collection: {}    Time of Collection: {}
                  Patient Name: {}    
                       Gender : {}    Age: {}
                      Ref. Dr : {}
                 Collected At : {} 
        ----------------------------------------------------------------------------------------
          Srl No                        Investigation / Particulars                  Rate
        ----------------------------------------------------------------------------------------
         """.format(bill_no, ref_no, dt_string, date_collection, time_collection, patient_name, 
                    patient_gender, patient_age, ref_doctor, collected_at))


#Test and pricing section
test_cunt = int(input("Enter no of test"))
test_count = 1
if ( test_cunt  >  0):
         test_name = input("Enter Test Name: ")
         test_price = float(input("Enter Test Price: "))
         patient_det()
         print("""
            {}                           {}                                   {}                   
         
         
                                          Total Amount: 
         """.format(test_count, test_name, test_price))
else:
    print("No Test Found")










