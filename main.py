#!/usr/bin/env python3
import os
import sys
import re
import time
import subprocess
import threading

# Make sure script is running as root
if os.geteuid() != 0:
    sys.exit("This script must be run as root!")

# Path to the log file (change to your actual log file path)
LOG_FILE = "/etc/log.txt"

# track already blocked ips
blocked_ips = set()

def read_new_log_entries(log_file, last_position):
    """
    Opens the log file and returns new lines added since last_position.
    """
    with open(log_file, 'r') as f:
        f.seek(last_position)
        new_entries = f.readlines()
        new_position = f.tell()
    return new_entries, new_position

def extract_ip_from_line(line):
    """
    Extracts the first IP address found in the given line using a regular expression.
    """
    match = re.search(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', line) #expresion to extract ip
    if match:
        return match.group(0)
    return None

def block_ip_address(ip):
    """
    Blocks the given IP address using iptables if it is not already blocked.
    """
    global blocked_ips
    if ip not in blocked_ips:
        print(f"[+] Blocking IP: {ip}")
        # Use iptables to drop traffic from the given IP address
        subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"], check=True)
        blocked_ips.add(ip)
    else:
        print(f"[!] IP {ip} is already blocked.")

def process_log_line(line):
    """
    Processes a single log line by extracting any IP address and launching a thread to block it.
    """
    ip = extract_ip_from_line(line)
    if ip:
        # Start a new thread to block the IP
        t = threading.Thread(target=block_ip_address, args=(ip,), daemon=True)
        t.start()

def monitor_logs():
    """
    Continuously monitors the log file for new entries and processes them.
    """
    # Start reading from the beginning; change to end-of-file if you want to ignore old entries
    last_position = 0
    print("[*] Monitoring log file for malicious IP addresses...")
    
    while True:
        try:
            new_entries, last_position = read_new_log_entries(LOG_FILE, last_position)
            if new_entries:
                for entry in new_entries:
                    entry = entry.strip()
                    if entry:  # ignore empty lines
                        print(f"[DEBUG] New log entry: {entry}")
                        process_log_line(entry)
            # Poll the file for new entries every second
            time.sleep(1)
        except FileNotFoundError: #try and catch
            print(f"[ERROR] Log file not found: {LOG_FILE}")
            time.sleep(5)
        except Exception as e:
            print(f"[ERROR] {e}")
            time.sleep(1)

if __name__ == "__main__": #ensures that the monitor_logs() function only runs when the script is executed directly, not when it's imported as a module into another script.
    monitor_logs()
