from netmiko import ConnectHandler, NetMikoTimeoutException
from getpass import getpass

username: str = input("Username: ")
password: str = getpass()

#  SSH function
def ssh(device: str, commands: list) -> dict:
    """
    This functions allows you to ssh to cisco devices and activate enable mode

    Args:
        device: FQDN or IP of the device
        commands: list of strings, each element is command

    Returns:
        Returns a dictionary which each key is the command we execute and the value is the output

    Raises:
        NetMikoTimeoutException: Timeout Exception
        EOFError: End of file error
        Exception: Unknown error
    """
    try:
        # Connection Handler
        connection = ConnectHandler(ip=device, device_type="cisco_ios", username=username, password=password, secret=password)
        connection.enable()
        # Dictionary comprehension for command and output
        command_output = {command:connection.send_command(command) for command in commands}
        connection.disconnect()
        return command_output
    except(NetMikoTimeoutException):
        print('Timeout to device ' + device)
    except(EOFError):
        print("End of file while attempting device " + device)
    except Exception as e:
        print('Unknown error: ' + f"{e}")

def main():
    # Device list
    devices: list = input("Enter devices, leave a space between them:\n ").split()
    # Commands list
    commands: list = input("Enter commands delimited by commas:\n ").split(',')
    # Loop through devices
    for device in devices:
        with open (f"{username}.md", "a") as f:
            print(f"Connecting to {device}")
            ssh(device, commands)

if __name__ == '__main__':
    main()
