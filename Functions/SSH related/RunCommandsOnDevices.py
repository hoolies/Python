from datetime import datetime                       # for timestamps
from re import sub                                  # for regular expressions
from getpass import getpass                         # for passwords
from netmiko import ConnectHandler                  # for connection
from concurrent.futures import ThreadPoolExecutor   # for multithreading

# Set the Start Time
time = datetime.now()
StartTime = time.replace(microsecond=0)

# Set the lists for devices and commands
devices = []
commands = []

# Get the credentials
username = input('Username: ')
password = getpass()

# Creates a file to save the output
file = open(f"{username}-{time.day}-{time.month}-{time.hour}{time.minute}{time.microsecond}.md", "w")
file.write(f'\nThe script started at: {StartTime}\n\n')


def whileloop(message):
    print(message)
    while True:
        line = input()
        if not line:
            pass
        if line.upper() == 'DONE':
           return commands
        if line:
            clearline = sub(r'\s+', ' ', line.strip())
            commands.append(clearline)



# Set the list with commands
commands = whileloop("Paste the commands.\n Once you are done, type done.\n ")


# Set the list with  wit the devices
devices = whileloop("Paste the devices.\n Once you are done, type done.\n ")


# Create concurrent function
def asynch(function, list):
    with ThreadPoolExecutor(max_workers=12) as executor:
        executor.map(function, list)


# Run a double loop for the devices and the commands
def ssh_connection(device, commands):
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
        for command in commands:
            # Check the time
            time = datetime.now()
            # Prints the name of the device and the command
            print(f'\n\nRunning {command} on {device} on {device} at {time}')
            # Write the command, the device and the time on file
            file.write(f'\n## {command} \n```\n')
            # Connect to the device and run the command
        CommandOutput = {command:connection.send_command(command) for command in commands}
        # Close the ssh connection
        connection.disconnect
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
