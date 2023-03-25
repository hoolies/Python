from netmiko import ConnectHandler, AuthenticationException, NetMikoTimeoutException, SSHException
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

#  SSH function
def ssh(device, commands):
    try:
        # Connection Handler    
        connection = ConnectHandler(ip=device, device_type="cisco_ios", username=username, password=password, secret=password)
        connection.enable()
        # Dictionary comprehension for command and output
        command_output = {command:connection.send_command(command) for command in commands}
        connection.disconnect
        return command_output
    except(AuthenticationException):
        print('Authentication failure: ' + device)
    except(NetMikoTimeoutException):
        print('Timeout to device ' + device)
    except(EOFError):
        print("End of file while attempting device " + device)
    except(SSHException):
        print('SSH might not be enabled for ' + device)
    except Exception as unknown_error:
        print('Uknown error: ' + unknown_error)