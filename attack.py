import re
import time
import subprocess
import os

snort_log_file = ""
blocked_ip = set()
last_position = 0

def extract_attacker_ips(log_file):
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
