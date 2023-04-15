import os


def main():
    # Get the username
    username = os.environ.get('USER')

    # Get the Home directory
    home = os.environ.get('HOME')

    # Get the OS
    OS = os.name

    # Set the path
    if OS == 'posix':
        path = home + '/Downloads/'
    else:
        path = home + '\Downloads\\'

    # Get all the files of a folder
    files = os.listdir(path)

    for file in files:
        extension = os.path.splitext(file)[1][1:]
        # Check if a folder exists for the extension
        if OS == 'posix':
            fullpath = f"{path}{extension}/"
        else:
            fullpath = f"{path}{extension}\\"
        if not os.path.exists(fullpath):
            os.mkdir(fullpath)
        # Move the files to the folder
        os.rename(path + file, fullpath + file)

if __name__ == '__main__':
    main()
