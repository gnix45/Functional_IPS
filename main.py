import re
import time
import subprocess
import os

snort_log_file = ""
blocked_ip = set()
last_position = 0

def read_new_log_entries(log_file, last_read_position):# by sharon
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
            
def extract_attacker_ips(log_file): #By Favour
    # define a function to extract attacker IPs from the log file
    with open(log_file, 'r') as f:
        # open the log file in read mode
        log_data = f.read()
        # use a regular regular expression to find all IP addresses in the log data
        ip_addresses = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', log_data)
        # use a list comprehension to filter out duplicate IP addresses and identify attackers IPs
        attacker_ips = [ip for ip in set(ip_addresses) if "attack" in log_data or "malicious" in log_data]
        # return the list of attackers IPs
        return attacker_ips
    
def block_ip_address(ip): #by favour
    """using ip tables in kali to blocked source ip"""
    if ip not in blocked_ip:#incase ip is not blocked
        print(f"[+] Blocking ip: {ip}")
        subprocess.run(["sudo","iptables","-A","INPUT","-s",ip,"-j","DROP"])#comand to block
        blocked_ip.add(ip)#add the ip to the list of blocked ip
    else:
        print("IP ALREADY BLOCKED")


"""to monitor snort logs"""
def monitor_logs():
    print("Monitoring Mode...")
    while True:
        log_line = read_new_log_entries()
        if log_line:
            attck_ip = extract_attacker_ips(log_line)
            for ip in attck_ip:
                block_ip_address(ip)
        time.sleep(1)    