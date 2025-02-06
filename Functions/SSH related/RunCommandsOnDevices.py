from collections.abc import Callable                # Type hinting
from concurrent.futures import ThreadPoolExecutor   # for multithreading
from datetime import datetime                       # for timestamps
from getpass import getpass                         # for passwords
from netmiko import ConnectHandler                  # for connection
from re import sub                                  # for regular expressions

# Set the Start Time
time = datetime.now()
StartTime = time.replace(microsecond=0)

# Get the credentials
username: str = input('Username: ')
password: str = getpass()

# Creates a file to save the output
file = open(f"{username}-{time.day}-{time.month}-{time.hour}{time.minute}{time.microsecond}.md", "w")
file.write(f'\nThe script started at: {StartTime}\n\n')

def whileloop(message: str, list: list) -> list:
    print(message)
    while True:
        line = input()
        if not line:
            pass
        if line.upper() == 'DONE':
           return list
        if line:
            clearline = sub(r'\s+', ' ', line.strip())
            list.append(clearline)


# Set the list with commands and the devices. functional way with correction/
commands: list = whileloop("Paste the commands.\n Once you are done, type done.\n ")
devices: list = whileloop("Paste the devices.\n Once you are done, type done.\n ")

# Create concurrent function
def asynch(function: Callable, list: list) -> None:
    with ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(function, list)


# Run a double loop for the devices and the commands
def ssh_connection(device: str, commands: list):
    try:
        print(f'Connecting to  {device}')
        connection = ConnectHandler(
            ip=device,
            device_type="cisco_ios",
            username=username,
            password=password,
            secret=password
        )
        # Connect to enabled mode
        connection.enable()
        # Run the commands
        file.write(f'# {device} \n')
        # Connect to the device and run the command
        CommandOutput = {command:connection.send_command(command) for command in commands}
        # Close the ssh connection
        connection.disconnect()
        # Return the output
        return CommandOutput
    # Exception handling
    except Exception as e:
        print(f'Error: {e}')


# Set the EndTime and the ExecutionTime
time = datetime.now()
EndTime = time.replace(microsecond=0)
ExecutionTime = EndTime - StartTime


file.write(f'\n\n\n\nThe script was executed successfully.\nFinished at {EndTime}.\nLasted for {ExecutionTime}')
file.close
