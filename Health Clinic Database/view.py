from Tkinter import *
import tkMessageBox
import tkFileDialog
import time, os
from model import Patient, Record
from controller import *
from controller import patients
import controller

#
# Health Clinic Database -- creates and stores personal health records 
#
# @author James Barney
# @date 2013-11-8
# @version 1.0
#


"""
Creates a form for the user to input data about the patient.
--Creates a new patient record
--Injury type
--Treatment type
"""

##################    Create Widgets    #################

def create_widgets_in_initial_frame():
    # Create the label for the frame
    initial_frame_label = Label(initial_frame, text='Welcome to the Health Clinic Database System')
    initial_frame_label.grid(column=1, row=0, pady=10, padx=10, columnspan=2)

    # Create the button for the frame
    initial_frame_quit_button = Button(initial_frame, text = "Quit", command = quit_program)
    initial_frame_quit_button.grid(column=1, row=1, pady=10)
    initial_frame_new_entry_button = Button(initial_frame, text = "New Entry", command = call_ID_frame_on_top)
    initial_frame_new_entry_button.grid(column=2, row=1, pady=10)

def create_widgets_in_login_frame():
    # Create the label for the frame
    login_frame_label = Label(login_frame, text='Please Log In Below')
    login_frame_label.grid(column=0, row=0, pady=10, padx=10)

    # Create the button for the frame
    login_frame_back_button = Button(login_frame, text = "Back", command = call_initial_frame_on_top)
    login_frame_back_button.grid(column=0, row=1, pady=10)
    login_frame_next_button = Button(login_frame, text = "Login", command = call_patient_frame_on_top)
    login_frame_next_button.grid(column=1, row=1, pady=10)

def create_widgets_in_ID_frame():
    # Create the label for the frame
    ID_frame_label = Label(ID_frame, text='Please enter Student ID:')
    ID_frame_label.grid(column=0, row=1, pady=10, padx=10)
    
    #Label(ID_frame,text="Student ID:").grid(row=1, column=0, sticky=E)
    student_id_field = StringVar()
    student_id_entry = Entry(ID_frame, width=30, textvariable=student_id_field)
    student_id_entry.grid(row=1, column=1)

    # Create the button for the frame
    ID_frame_back_button = Button(ID_frame, text = "Back", command = call_initial_frame_on_top)
    ID_frame_back_button.grid(column=0, row=2, pady=10)
    ID_frame_next_button = Button(ID_frame, text = "Submit", command = lambda: new_record(student_id_entry.get()) )
    ID_frame_next_button.grid(column=1, row=2, pady=10)

def create_widgets_in_patient_frame(patient):
    # Create the label for the frame
    patient_ID = patient.stu_id
    #patient_ID = "107566575"
    patient_frame_label = Label(patient_frame, text='Patient ' + str(patient_ID))
    patient_frame_label.grid(column=0, row=0, pady=10, padx=10, columnspan = 2)

    # Create the button for the frame
    patient_frame_back_button = Button(patient_frame, text = "Back", command = call_ID_frame_on_top)
    patient_frame_back_button.grid(column=0, row=1, pady=10)
    patient_frame_record_button = Button(patient_frame, text = "New Record", command = lambda: new_record(patient_ID))
    patient_frame_record_button.grid(column=1, row=1, pady=10)
    
def create_widgets_in_new_entry_frame():
    # Create the label for the frame
    new_entry_label = Label(entry_frame, text='Entry Form')
    new_entry_label.grid(column=0, row=0, pady=10, padx=10)

    # Create the button for the frame
    new_entry_back_button = Button(entry_frame, text = "Back", command = call_login_frame_on_top)
    new_entry_back_button.grid(column=0, row=1, pady=10)
    new_entry_quit_button = Button(entry_frame, text = "Quit", command = quit_program)
    new_entry_quit_button.grid(column=1, row=1, pady=10)

def create_widgets_in_new_patient_frame():
    # Create the label for the frame
    new_patient_label = Label(new_patient_frame, text='New Patient Form')
    new_patient_label.grid(column=0, row=0, pady=10, padx=10)
    
    first_name_label = Label(new_patient_frame, text='First Name: ')
    first_name_label.grid(column=0, row=1, pady=10, padx=10)
    first_name_text = StringVar()
    first_name_field = Entry(new_patient_frame, width=20, textvariable=first_name_text).grid(column=1,row=1)
    
    last_name_label = Label(new_patient_frame, text='Last Name: ')
    last_name_label.grid(column=0, row=2, pady=10, padx=10)
    last_name_text = StringVar()
    last_name_field = Entry(new_patient_frame, width=20, textvariable=last_name_text).grid(column=1,row=2)
    
    stu_id_label = Label(new_patient_frame, text='Student ID: ')
    stu_id_label.grid(column=0, row=3, pady=10, padx=10)
    stu_id_text = StringVar()
    stu_id_field = Entry(new_patient_frame, width=20, textvariable=stu_id_text).grid(column=1,row=3)
    
    email_label = Label(new_patient_frame, text='Student Email: ')
    email_label.grid(column=0, row=4, pady=10, padx=10)
    email_text = StringVar()
    email_field = Entry(new_patient_frame, width=20, textvariable=email_text).grid(column=1,row=4)
    
    student_phone_label = Label(new_patient_frame, text='Student Phone: ')
    student_phone_label.grid(column=0, row=5, pady=10, padx=10)
    student_phone_text = StringVar()
    student_phone_field = Entry(new_patient_frame, width=20, textvariable=student_phone_text).grid(column=1,row=5)
    
    emergency_label = Label(new_patient_frame, text='Emergency Contact: ')
    emergency_label.grid(column=0, row=6, pady=10, padx=10)
    emergency_text = StringVar()
    emergency_field = Entry(new_patient_frame, width=20, textvariable=emergency_text).grid(column=1,row=6)
    
    emergency_phone_label = Label(new_patient_frame, text='Emergency Phone: ')
    emergency_phone_label.grid(column=0, row=7, pady=10, padx=10)
    emergency_phone_text = StringVar()
    emergency_phone_field = Entry(new_patient_frame, width=20, textvariable=emergency_phone_text).grid(column=1,row=7)

    # Create the button for the frame
    new_patient_back_button = Button(new_patient_frame, text = "Back", command = call_ID_frame_on_top)
    new_patient_back_button.grid(column=0, row=8, pady=10)
    new_patient_next_button = Button(new_patient_frame, text = "Create...", command = lambda: create_patient(first_name_text.get(),last_name_text.get(),stu_id_text.get(),email_text.get(),student_phone_text.get(),emergency_text.get(),emergency_phone_text.get()))
    new_patient_next_button.grid(column=1, row=8, pady=10)

####################    Create Frames    ####################

def call_initial_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    forget_frames(initial_frame)
    initial_frame.grid(column=0, row=0, padx=20, pady=5)

def call_login_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    forget_frames(login_frame)
    login_frame.grid(column=0, row=0, padx=20, pady=5)

def call_patient_frame_on_top(patient):
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    forget_frames(patient_frame)
    create_widgets_in_patient_frame(patient)
    patient_frame.grid(column=0, row=0, padx=20, pady=5)
    
def call_new_entry_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    forget_frames(entry_frame)
    entry_frame.grid(column=0, row=0, padx=20, pady=5)

def call_ID_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    forget_frames(ID_frame)
    ID_frame.grid(column=0, row=0, padx=20, pady=5)

def call_new_patient_frame_on_top():
    forget_frames(new_patient_frame)
    new_patient_frame.grid(column=0, row=0, padx=20, pady=5)


##################    Functionality    #########################

def quit_program():
    root_window.destroy()
    
def forget_frames(in_frame):
    #forgets every frame except the one passed in
    for frame in frame_list:
        if in_frame is not frame:
            frame.grid_forget()
            
def new_record(patient_ID):
    #creates a new Record for the Patient
    #~ print patient_ID
    try:
        patient = controller.get_patient(patient_ID)
        record = Record()
    except:
        call_new_patient_frame_on_top()
        
def create_patient(first_name, last_name, stu_id, email, phone, emergency, emergency_phone):
    patient = Patient(first_name, last_name, stu_id, email, phone, emergency, emergency_phone)
    controller.new_patient(patient)
    #create_widgets_in_patient_frame(patient)
    call_patient_frame_on_top(patient)
        

##################    Main Program    #########################

root_window = Tk()
root_window.title("Health Clinic Database Form")

# Define window size
window_width = 1000
window_height = 800

# Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions. 
initial_frame=Frame(root_window, width=window_width, height=window_height)
initial_frame['borderwidth'] = 2
initial_frame['relief'] = 'sunken'
initial_frame.grid(column=0, row=0, padx=20, pady=5)

login_frame=Frame(root_window, width=window_width, height=window_height)
login_frame['borderwidth'] = 2
login_frame['relief'] = 'sunken'
login_frame.grid(column=0, row=0, padx=20, pady=5)

patient_frame=Frame(root_window, width=window_width, height=window_height)
patient_frame['borderwidth'] = 2
patient_frame['relief'] = 'sunken'
patient_frame.grid(column=0, row=0, padx=20, pady=5)

entry_frame=Frame(root_window, width=window_width, height=window_height)
entry_frame['borderwidth'] = 2
entry_frame['relief'] = 'sunken'
entry_frame.grid(column=0, row=0, padx=20, pady=5)

ID_frame=Frame(root_window, width=window_width, height=window_height)
ID_frame['borderwidth'] = 2
ID_frame['relief'] = 'sunken'
ID_frame.grid(column=0, row=0, padx=20, pady=5)

new_patient_frame=Frame(root_window, width=window_width, height=window_height)
new_patient_frame['borderwidth'] = 2
new_patient_frame['relief'] = 'sunken'
new_patient_frame.grid(column=0, row=0, padx=20, pady=5)

# Create all widgets in all frames
#create_widgets_in_patient_frame()
create_widgets_in_login_frame()
create_widgets_in_initial_frame()
create_widgets_in_new_entry_frame()
create_widgets_in_ID_frame()
create_widgets_in_new_patient_frame()

frame_list = [initial_frame, login_frame, patient_frame, entry_frame, ID_frame, new_patient_frame]

# Hide all frames in reverse order, but leave first frame visible (unhidden).
forget_frames(initial_frame)


root_window.mainloop()
