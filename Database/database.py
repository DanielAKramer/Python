# Database program
#
#  A simple database, records are list of
#       [Firstname, Lastname, Age]
#
#  The database file has lines of the form:
#     last_name : first_name : age
#
# Daniel  Kramer
# Database Program
import sys
import database_mod
#===============================================================================
def main():
    # Database file name
    database_file = 'database.txt'

    # Input database data
    db = database_mod.open_db(database_file)
    
    # Show menu initially
    show_menu()

    # Main loop
    while True:
        # Prompt, input choice
        choice = input("Please enter a choice, 'm' for menu: ")
        if choice == 'l':
            # Lookup last name
            name = input("Please enter a last name: ")
            idx = database_mod.lookup_last_name(db, name)
            if idx != None:
                 database_mod.output_record(db[idx])
            else:
                 output_error("'%s' not in database" % (name))
        elif choice == 'f':
            # Lookup first name
            name = input("Please enter a first name: ")
            idx = database_mod.lookup_first_name(db, name)
            if idx != None:
                 database_mod.output_record(db[idx])
            else:
                 output_error("'%s' not in database" % (name))

        elif choice == 'a':
            # Lookup age
            age = input("Please enter a age: ")
            idx = database_mod.lookup_age(db, age)
            if idx != None:
                 database_mod.output_record(db[idx])
            else:
                 output_error("'%s' not in database" % (age))

        elif choice == 'o':
            # Output entire database
            database_mod.output_all(db)

        elif choice == 'n':
            # Add an entry to the database
            last_name  = input("Enter last name:  ")
            first_name = input("Enter first name: ")
            age     = input("Enter age:     ")
            database_mod.add_record(db, first_name, last_name, age)

        elif choice == 'm':
            # Output the menu
            show_menu()

        elif choice == 'x' or choice == 'q':
            break

        else:
            output_error("Invalid choice: '%s'" % (choice))

    # Save database data
    database_mod.close_db(db, database_file)

#===============================================================================
def output_error(msg):
    # Output error message
    print(msg)

#===============================================================================
def show_menu():
     print('  l. Lookup by last name')
     print('  f. Lookup by first name')
     print('  a. Lookup by age')
     print('  o. Output all')
     print('  n. Add name and age')
     print('  m. Show this menu')
     print('  x. Exit')

#===============================================================================
# Call the main function
main()
