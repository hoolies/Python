import datetime                                                     # for timestamps
import re                                                           # for regular expressions
import getpass                                                      # for passwords
import netmiko                                                      # for connection


# Set the Start Time
time = datetime.datetime.now()
StartTime = time.replace(microsecond=0)

# Set the lists for devices and commands
devices = []
commands = []

# Get the credentials
username = input('Username: ')
password = getpass.getpass('Password: ')

# Creates a file to save the output
file = open(f"{username}-{time.day}-{time.month}-{time.hour}{time.minute}{time.microsecond}.txt", "w")
file.write(f'\nThe script started at: {StartTime}\n\n')

# Set the list with commands    
print("Paste the commands.\n Once you are done, type done.\n ")
while True:
    line = input()
    if line == '':
        pass
    if line == "Done" or line == "done" or line == 'DONE':
        break
    if line:
        clearline = re.sub(r'\s+', ' ', line.rstrip())
        noice = clearline.lstrip()
        commands.append(noice)


# Set the list with  wit the devices
print("Paste the devices.\n Once you are done, type done.\n ")
while True:
    line = input()
    if line == '':
        pass
    if line == "Done" or line == "done" or line == 'DONE':
        break
    if line:
        clearline = re.sub(r'\s+', ' ', line.rstrip())
        noice = clearline.lstrip()
        devices.append(noice)


# Run a double loop for the devices and the commands
for device in devices:
    print(f'Connecting to  {device}')
    connection = netmiko.ConnectHandler(ip=device, device_type="cisco_ios",username=username, password=password, secret=password)
    # Connect to enabled mode
    connection.enable()
    # Run the commands
    file.write(f'# {device} \n')
    for command in commands:
        # Check the time
        time = datetime.datetime.now()
        # Prints the name of the device and the command 
        print(f'\n\nRunning {command} on {device} on {device} at {time}')
        # Write the command, the device and the time on file 
        file.write(f'\n## {command} \n```\n')
        # Connect to the device and run the command
        CommandOutput = connection.send_command(command)
        # Saves the output in a list, each line an entry
        lines = CommandOutput.splitlines(True)
        # Prints lines on screen and saves them to a file
        for line in lines:
            print(f'{line}')
            file.write(f'{line}')
        file.write(f'\n```\n')
        file.write(f'\n---\n')
    # Close the ssh connection
    connection.disconnect

# Set the EndTime and the ExecutionTime
time = datetime.datetime.now()
EndTime = time.replace(microsecond=0)
ExecutionTime = EndTime - StartTime

file.write(f'\n\n\n\nThe script was executed successfully.\nFinished at {EndTime}.\nLasted for {ExecutionTime}')
file.close
