import re
from os import path
from colorama import Fore as c
from googleapiclient.discovery import build
from tqdm import tqdm
import csv


def validate_api(key: str) -> None:
    """_summary_ : to validate the user input."""
    if key:
        pass
    else:
        exitprog("API key Invalid! ❌", 1)
    youtube = build("youtube", "v3", developerKey=key)
    request = youtube.commentThreads().list(
        part="id", maxResults=0, videoId="fT2KhJ8W-Kg"
    )
    try:
        for _ in tqdm(range(5), desc="Validating API key . . ."):
            request.execute()
    except Exception:
        exitprog(f"API key {key} is invalid! ❌", 1)
    else:
        print("API Key is Valid ✔️")


def get_key():
    """_summary_ : Function to prompt the user for their API key

    Returns:
        string : The api key
    """
    API_KEY = ""
    if path.isfile(".env"):
        with open(".env") as env:
            API_KEY = env.readline()
        print(c.GREEN + "Got API KEY! ✔️")
    else:
        print(
            c.YELLOW
            + "You can get your API key from here : "
            + c.BLUE
            + "https://console.cloud.google.com/apis/library/youtube.googleapis.com"
        )
        API_KEY = input(c.WHITE + "Enter API Key (Use Ctrl+Shift+V to paste):")
        validate_api(API_KEY)
        print(c.GREEN + "Saving API key . . " + c.WHITE + ". ")
        with open(".env", "w") as env:
            env.write(API_KEY)
    return API_KEY


def theinput():
    return input(c.LIGHTBLUE_EX + "Enter a Youtube URL >" + c.WHITE + "> ")


def isvalid(url):
    """_summary_ : Validate whether the given url belongs to a youtube video or not

    Args:
        url (_str_): The video url

    Returns:
        _bool_
    """
    global regex
    regex = r"https:\/\/(?:youtu\.be\/|www\.youtube\.com\/watch\?v=)([^&#]+)"
    if re.search(regex, url):
        return True
    else:
        print(
            c.RED + "Please enter the URL to a Youtube Video ",
            c.WHITE + "Example : https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            sep="\n",
        )
        return False


def getid(url):
    """_summary_ : Extract video ID from the youtube URL for the youtube API

    Args:
        url (_str_): The video url
    Returns: The video id
    """
    id = re.search(regex, url).group(1)
    print(c.LIGHTGREEN_EX + "Video ID Found : " + c.WHITE + id)
    return id


def exitprog(reason="", code=0):
    if reason:
        print(c.RED + reason)

    print(c.RED + "\nExiting the Program . . " + c.WHITE + ".")
    exit(code)


def get_comments(API_KEY, vidId, results=20, allComments=False):
    youtube = build("youtube", "v3", developerKey=API_KEY)

    part = "id,snippet"

    def getComments():
        request = youtube.commentThreads().list(
            part=part, maxResults=results, order="time", videoId=vidId
        )
        for _ in tqdm(range(10), desc=c.GREEN + "Fetching  Comments . . ."):
            response = request.execute()
        #  format the response dict to return a list of comments

        with open(f"{vidId}_comments.csv", "w", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Author", "Likes", "Comment"])

            for comment in response["items"]:
                writer.writerow(
                    [
                        comment["snippet"]["topLevelComment"]["snippet"][
                            "authorDisplayName"
                        ],
                        comment["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                        comment["snippet"]["topLevelComment"]["snippet"][
                            "textOriginal"
                        ],
                    ]
                )
        print(
            c.GREEN + "Comments saved to file " + c.WHITE + f"{vidId}_comments.csv ✔️"
        )

    def getAllComments():
        ...

        exitprog("Cannot get all comments , feature not implemented yet 😞")
        # TODO: Implement getAllComments functionality
        # basically have to write a recursive function that calls itself with the next page token and then we have a list of responses
        # that would be [dict,dict,dict] where each dict is a response
        # then we have to merge all the comments from all the responses into a single list
        # and then we have to return that list

    if allComments or results > 100:
        responses = getAllComments()
    else:
        response = getComments()


def get_number_of_comments():
    try:
        results = int(
            input(
                c.YELLOW
                + "Enter the number of results you want to request (max is 100)"
                + c.WHITE
                + ": "
            )
        )
    except Exception:
        print(c.RED + "Invalid character")
        print(c.YELLOW + "Taking the default value as 20")
        results = 20

    return results


def main():
    API_KEY = get_key()
    while True:
        URL = theinput()
        if isvalid(URL):
            break
        else:
            continue

    id = getid(URL)
    allComments = input(
        c.YELLOW + "Do you want to get all the comments ?[Y/N] " + c.WHITE + ": "
    )
    if allComments.upper() == "N":
        allComments = False
        results = get_number_of_comments()
    elif allComments.upper() == "Y":
        allComments = True
        results = 100
    else:
        exitprog("Invalid Choice!")

    get_comments(API_KEY, id, results, allComments)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        exitprog()
