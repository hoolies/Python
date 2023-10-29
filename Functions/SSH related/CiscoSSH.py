from netmiko import ConnectHandler, NetMikoTimeoutException
from getpass import getpass

username: str = input("Username: ")
password: str = getpass()

#  SSH function
def ssh(device: str, commands: str) -> dict:
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
    return command_output

def main():
    # Device list
    devices = input("Enter devices, leave a space between them:\n ").split()
    # Commands list
    commands = input("Enter commands leave a space between them:\n ").split()
    # Loop through devices
    for device in devices:
        with open (f"{username}.md", "a") as f:
            print(f"Connecting to {device}")
            ssh(device, commands)

if __name__ == '__main__':
    main()
