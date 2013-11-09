
# This class models the various objects used in the database
# Patients are made up of zero or many entries.
#
# @author James Barney
# @date 2013-11-8
# @version 1.0
#

class Patient:
    def __init__(self, first_name, last_name, stu_id, emergency=None, email=None, phone=None):
        self.first_name = first_name
        self.last_name = last_name
        self.stu_id = stu_id
        self.emergency = emergency
        self.email = email
        self.phone = phone


class Entry:
    def __init__(self, datetime, sport, injury, treatment, follow_up):
        self.datetime = datetime
        self.sport = sport
        self.injury = injury
        self.treatment = treatment
        self.follow_up = follow_up
