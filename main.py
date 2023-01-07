import re
from colorama import Fore as c


def theinput():
    return input(c.LIGHTGREEN_EX + "Enter a Youtube URL >> ")


def isvalid(URL):
    if re.search(r"youtube.com", URL):
        return True
    else:
        print(c.RED + "Please Enter a Youtube URL ")
        return False


def main():
    while True:
        if isvalid(theinput()):
            break
        else:
            continue

if __name__ == "__main__":
    main()
# Input loop



