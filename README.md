# Snort Log Monitor and IP Blocker

![Snort Monitor](https://img.shields.io/badge/status-active-brightgreen.svg)

## 📌 Overview
This script monitors a Snort log file for potential attacks and automatically blocks attacker IPs using `iptables`. It continuously reads new log entries, extracts attacker IP addresses, and blocks them if necessary.

## ✨ Features
✅ Reads new log entries in real-time.  
✅ Extracts attacker IPs using regex.  
✅ Blocks malicious IPs using `iptables` (Linux-based firewall rule management).  
✅ Runs in a loop for continuous monitoring.

## 🛠 Requirements
- Python 3
- Snort (configured to generate log files)
- Linux system (with `iptables` installed)
- Root privileges (required for modifying firewall rules)

## 🚀 Installation
```sh
# Clone this repository
git clone https://github.com/gnix45/Functional_IPS.git
cd Functional_IPS

# Ensure Python is installed on your system
python3 --version
```

Modify the `log_file` variable in `main.py` to point to the correct Snort log file path.

## 🔥 Usage
Run the script with:
```sh
sudo python3 main.py
```
(Use `sudo` to allow `iptables` commands to execute.)

The script will continuously monitor the log file and block malicious IPs.

## 🧩 Functions Breakdown
- **`read_new_log_entries(log_file, last_read_position)`**: Reads new entries from the Snort log file.
- **`extract_attacker_ips(log_file)`**: Extracts attacker IPs using regex.
- **`block_ip_address(ip)`**: Blocks the identified malicious IPs using `iptables`.
- **`monitor_logs()`**: Continuously monitors logs and calls the necessary functions.

## ⚠️ Notes
- The script requires administrative privileges to run `iptables` commands.
- Ensure Snort is correctly configured to log attack attempts.
- Modify the `log_file` variable with the actual log file path.

## 👥 Authors
- **Sharon**  
- **Favour**
## Supervisor
- **PAVEL**

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer
Use this script responsibly. Blocking IP addresses without proper verification may lead to unintended network disruptions.

---

🌟 **Star this repo if you find it useful!** ⭐
