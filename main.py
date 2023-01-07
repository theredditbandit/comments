import re
from colorama import Fore as c


def theinput():
    return input(c.LIGHTGREEN_EX + "Enter a Youtube URL >> ")


def isvalid(url):
    """_summary_ : Validate whether the given url belongs to a youtube video or not

    Args:
        url (_str_): The video url

    Returns:
        _bool_
    """
    if re.search(r"youtube.com/watch\?v",url) or re.search(r"youtu.be",url):
        return True
    else:
        print(c.RED + "Please enter the URL to a Youtube Video ",c.WHITE + "Example : https://www.youtube.com/watch?v=dQw4w9WgXcQ",sep="\n")
        return False

def getid(url):
    """_summary_ : Extract video ID from the youtube URL for the youtube API

    Args:
        url (_str_): The video url
    Returns: The video id
    """
    id = re.search(r"^https:\/\/(?:youtu\.be\/|www\.youtube\.com\/watch\?v=)([^&#]+)", url).group(1)
    print(c.YELLOW + "Video ID Found : " + c.WHITE + id)
    return id


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




