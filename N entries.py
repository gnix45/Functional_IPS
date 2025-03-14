import os
import time

#define a function 
def read_new_log_entries(log_file, last_read_position):
#open the log file in read mode
    with open(log_file, 'r') as f:
        #move the file pointer to the last read position
        f.seek(last_read_position)
        #read all lines from the current file position till the end
        new_entries = f.readlines()
        #return the new log_enteries and the current file position
        return new_entries, f.tell()
    
    #specify the path to the log file
    log_file = 'path/to/your/log/file.log'
    #set up the last read position to 0
    last_read_position = 0
    while True:
        #bring the function to the new log entries
        new_entries, last_read_position = read_new_log_entries(log_file, last_read_position)
        #start over the new log entries
        for entry in new_entries:
            #print each log entry
            print(entry.strip())
            #pause for 3 seconds before checking again
            time.sleep(3)
    


