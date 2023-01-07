import re
from colorama import Fore as c


def theinput():
    return input(c.LIGHTGREEN_EX + "Enter a Youtube URL >> ")


def isvalid(URL):
    if re.search(r"youtube.com/watch\?v",URL):
        return True
    else:
        print(c.RED + "Please enter the URL to a Youtube Video ",c.WHITE + "Example : https://www.youtube.com/watch?v=dQw4w9WgXcQ",sep="\n")
        return False

def getid(): # to get video ID from the youtube URL for the youtube API
    ...


def main():
    # input loop
    while True:
        URL = theinput()
        if isvalid(URL):
            break
        else:
            continue
    
    id = getid(URL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        print(c.RED + "\nExiting the Program . . " + c.WHITE + ".")
        exit(0)




