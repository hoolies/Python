import netmiko
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

#  SSH function
def ssh(device, commands):
    try:
        # Connection Handler    
        connection = netmiko.ConnectHandler(ip=device, device_type="cisco_ios", username=username, password=password, secret=password)
        connection.enable()
        # Dictionary comprehension for command and output
        command_output = {command:connection.send_command(command) for command in commands}
        connection.disconnect
        return command_output
    except(netmiko.AuthenticationException):
        print('Authentication failure: ' + device)
    except(netmiko.NetMikoTimeoutException):
        print('Timeout to device ' + device)
    except(EOFError):
        print("End of file while attempting device " + device)
    except(netmiko.SSHException):
        print('SSH might not be enabled for ' + device)
    except Exception as unknown_error:
        print('Uknown error: ' + unknown_error)
