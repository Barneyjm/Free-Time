
# This class models the various objects used in the database
# Patients are made up of zero or many entries.
#
# @author James Barney
# @date 2013-11-8
# @version 1.0
#

class Patient:
    def __init__(self, first_name, last_name, stu_id, email=None, phone=None, emergency=None, emergency_phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.stu_id = stu_id
        self.emergency = emergency
        self.emergency_phone = emergency_phone
        self.email = email
        self.phone = phone
        self.records = []
    
    def create_patient():
        self.patient = [
                   {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'stu_id': self.stu_id,
                    'email': self.email,
                    'phone': self.phone,
                    'emergency': self.emergency,
                    'emergency_phone': self.emergency_phone,
                    'records': []
                   }
                  ]
        
    def keys(self):
        return self.patient.keys()

class Record:
    def __init__(self, datetime, sport, injury, treatment, follow_up):
        self.datetime = datetime
        self.sport = sport
        self.injury = injury
        self.treatment = treatment
        self.follow_up = follow_up
        
    def create_record():
            record = [
                       {
                        'datetime': self.datetime,
                        'sport': self.sport,
                        'stu_id': self.stu_id,
                        'injury': self.injury,
                        'treatment': self.treatment,
                        'follow_up': self.follow_up,
                       }
                      ]
            return record
