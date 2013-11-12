import pymongo
import subprocess
from pymongo import MongoClient

# Controls dataflow to and from the health clinic database.
#
# @author James Barney
# @date 2013-11-8
# @version 1.0
#

client = MongoClient('localhost', 27017)

healthDB = client['health_database']

patients = healthDB['patient_collection']

def new_patient(patient):
    print patient.stu_id
    #~ patients.insert(patient)

def get_patient(patient_ID):
    return patients.find_one(patient_ID)
    
def store_record(patient_ID, record):
    patients[patient_ID].insert(record)
    
