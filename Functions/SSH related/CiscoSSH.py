from netmiko import ConnectHandler, NetMikoTimeoutException
from getpass import getpass

username = input("Username: ")
password = getpass()

#  SSH function
def ssh(device, commands):
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
    devices = input("Enter device list: ").split()
    # Commands list
    commands = input("Enter commands list: ").split()


if __name__ == '__main__':
    main()