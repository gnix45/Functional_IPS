import re
import time
import subprocess
import os


snort_log_file = ""
blocked_ip = set()
last_position = 0


def block_ip_address(ip): #by favour
    """using ip tables in kali to blocked source ip"""
    if ip not in blocked_ip:#incase ip is not blocked
        print(f"[+] Blocking ip: {ip}")
        subprocess.run(["sudo","iptables","-A","INPUT","-s",ip,"-j","DROP"])#comand to block
        blocked_ip.add(ip)#add the ip to the list of blocked ip
    else:
        print("IP ALREADY BLOCKED")