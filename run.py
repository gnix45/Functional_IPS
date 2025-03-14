import subprocess
def run_snort_log_script():#Define a function to run a snort_log_script
    try:
        subprocess.run(["python"], check=True) # run script using python interpreter
        print(f"Snort log script executed successfully.")#print successfull message
    except subprocess.CalledProcessError as e:#handle calledprocessorerror exceptions
        print(f"Error running Snort log script: {e}")#print error


run_snort_log_script()
