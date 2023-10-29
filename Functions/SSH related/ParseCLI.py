"""This script use RegEx to parse CLI"""
from re import sub                                       # for RegEx



def ParseCli(self):
    """Parse the code to space delimiter"""
    # Strip the extra empty lines
    new = self.strip('\n')
    # Split the string in lines
    lines = new.splitlines(True)
    # Initialize self and creates a list
    self = []
    # Runs a loop for each line in the CLI output
    for line in lines:
        # Merge many spaces to one space
        monospace = sub(r'\s+', ' ', line)
        # Remove spaces from the end of the line
        SpaceAtTheEnd = sub(r'\s$', '', monospace)
        # Splits the line with space as delimiter
        output = SpaceAtTheEnd.split(' ')
        # Append the line to the list
        self.append(output)
    # Return the CLI output as a list within a list, every line is an list and every word an entry
    return(self)

def main():
    """Main Function"""
    command_output = input('Enter the commands: ')
    output = ParseCli(command_output)
    print(output)



# If not imported
if __name__ == '__main__':
    main()
