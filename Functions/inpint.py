def inpint(message: str) -> int:
    while True:
        try:
            UserInput = int(input(message))
        except ValueError:
            print("Not an integer, try again!")
            continue
        else:
            return UserInput