
class Robot():
    pass


if __name__ == "__main__":
    try:
        r = Robot()

        while True:

            userInput = input("Please enter [x, y] points:")
            print (userInput, type(list))

    except KeyboardInterrupt:
        print "\nExiting..."
