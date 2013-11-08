from Tkinter import *
import tkMessageBox
import tkFileDialog
import time, os

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
    initial_frame_label.grid(column=0, row=0, pady=10, padx=10)

    # Create the button for the frame
    initial_frame_quit_button = Button(initial_frame, text = "Quit", command = quit_program)
    initial_frame_quit_button.grid(column=0, row=1, pady=10)
    initial_frame_next_button = Button(initial_frame, text = "Login", command = call_login_frame_on_top)
    initial_frame_next_button.grid(column=1, row=1, pady=10)

def create_widgets_in_login_frame():
    # Create the label for the frame
    login_frame_label = Label(login_frame, text='Please Log In Below')
    login_frame_label.grid(column=0, row=0, pady=10, padx=10)

    # Create the button for the frame
    login_frame_back_button = Button(login_frame, text = "Back", command = call_initial_frame_on_top)
    login_frame_back_button.grid(column=0, row=1, pady=10)
    login_frame_next_button = Button(login_frame, text = "Login", command = call_patient_frame_on_top)
    login_frame_next_button.grid(column=1, row=1, pady=10)

def create_widgets_in_patient_frame():
    # Create the label for the frame
    patient_frame_label = Label(patient_frame, text='Patient Form')
    patient_frame_label.grid(column=0, row=0, pady=10, padx=10)

    # Create the button for the frame
    patient_frame_back_button = Button(patient_frame, text = "Back", command = call_login_frame_on_top)
    patient_frame_back_button.grid(column=0, row=1, pady=10)
    patient_frame_quit_button = Button(patient_frame, text = "Quit", command = quit_program)
    patient_frame_quit_button.grid(column=1, row=1, pady=10)


####################    Create Frames    ####################

def call_initial_frame_on_top():
    # This function can be called only from the second window.
    # Hide the second window and show the first window.
    login_frame.grid_forget()
    initial_frame.grid(column=0, row=0, padx=20, pady=5)

def call_login_frame_on_top():
    # This function can be called from the first and third windows.
    # Hide the first and third windows and show the second window.
    initial_frame.grid_forget()
    patient_frame.grid_forget()
    login_frame.grid(column=0, row=0, padx=20, pady=5)

def call_patient_frame_on_top():
    # This function can only be called from the second window.
    # Hide the second window and show the third window.
    login_frame.grid_forget()
    patient_frame.grid(column=0, row=0, padx=20, pady=5)


##################    Functionality    #########################

def quit_program():
    root_window.destroy()
        

##################    Main Program    #########################

root_window = Tk()
root_window.title("Health Clinic Database Form")

# Define window size
window_width = 200
window_height = 100

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

# Create all widgets to all frames
create_widgets_in_patient_frame()
create_widgets_in_login_frame()
create_widgets_in_initial_frame()

# Hide all frames in reverse order, but leave first frame visible (unhidden).
patient_frame.grid_forget()
login_frame.grid_forget()

root_window.mainloop()
