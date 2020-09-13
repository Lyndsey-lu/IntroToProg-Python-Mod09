# ------------------------------------------------------------------------ #
# Title: Main.py (Psuedo-code copied from Listing 13) Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# LHolmes,1.8.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
import DataClasses
import ProcessingClasses
import IOClasses

# Main Body of Script  ---------------------------------------------------- #

# Load data from file into a list of employee objects when script starts
list_of_employees = ProcessingClasses.DatabaseProcessor.read_employees_from_file("EmployeeData.txt")

while(True):
    # Show user a menu of options
    IOClasses.EmployeeIO.print_menu_items()
    # Get user's menu option choice
    choice = IOClasses.EmployeeIO.input_menu_options()
    
    # Show user current data in the list of employee objects
    if choice == 1:
        IOClasses.EmployeeIO.print_current_list_items(list_of_employees)

    # Let user add data to the list of employee objects
    elif choice == 2:
        new_employee = IOClasses.EmployeeIO.input_employee_data()
        list_of_employees.append(new_employee)

    # let user save current data to file
    elif choice == 3:
        ProcessingClasses.FileProcessor.save_data_to_file("EmployeeData.txt", list_of_employees)

    # Let user exit program
    elif choice == 4:
        break
   
# Main Body of Script  ---------------------------------------------------- #
