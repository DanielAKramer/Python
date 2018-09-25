# Database module
# Daniel  Kramer
# Database Program
file_name = 'database.txt'
#===============================================================================
def open_db(file_name):
    # Open the file whose name is in the variable file_name
    # Exit if unsuccessful
    try:
        in_file = open(file_name)
    except:
        print("Couldn't open file:", file_name)
        exit(1)
        
    # Var to accumulate data in
    data = []
    
    # Open succeeded, read lines and print with line number
    while True:
        # Input a line
        line = in_file.readline()

        # If line is empty we are done, exit the loop
        if line == "":
            break

        # First split
        items = line.split(':')
        
        # Give names to sublist components
        last_name  = items[0].strip()
        first_name = items[1].strip()
        age        = items[2].strip()

        # Add data to the main list
        record = [ last_name, first_name, age]
        data.append(record)

        # Format the output
        msg = '%s - %s - %s' % (last_name, first_name, age)
     
        #print(msg)

    # Close file when done
    in_file.close()

    return data

#===============================================================================
def output_all(data):
    idx = 0
    while idx < len(data):
        # Give names to sublist items
        last_name  = data[idx][0]
        first_name = data[idx][1]
        age        = data[idx][2]
        
        # Create output message
        msg = '%s %s %s' % (last_name, first_name, age)

        # Output
        print(msg)
        idx = idx + 1
        
#===============================================================================
def lookup_last_name(data, name):
    

    idx = 0
    
    while idx < len(data):

        if data[idx][0] == name:

            return idx

        idx = idx + 1

    else:
            
        return None
    
     
#===============================================================================
def lookup_first_name(data, name):
    
    idx = 0
    
    while idx < len(data):

        if data[idx][1] == name:

            return idx

        idx = idx + 1

    else:
            
        return None
#===============================================================================
def lookup_age(data, age):
    
    idx = 0
    
    while idx < len(data):

        if data[idx][2] == age:

            return idx

        idx = idx + 1

    else:
            
        return None
#===============================================================================
def add_record(data, last_name, first_name, age):

    record = [ last_name, first_name, age]
    data.append(record)

#===============================================================================
def close_db(data, file_name):

    in_file = open(file_name, 'w')

    idx = 0
    
    while idx < len(data):

        last_name  = data[idx][0]
        first_name = data[idx][1]
        age        = data[idx][2] 

        in_file.write('%s : %s : %s\n' % (last_name, first_name, age))

        idx = idx + 1 
           
    in_file.close()
        
 

 
#===============================================================================
def output_record(eq_record):
        msg = '%s, %s %s' % (eq_record[0], eq_record[1], eq_record[2])
        print(msg)

#===============================================================================

