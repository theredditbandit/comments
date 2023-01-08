import pytest
from main import isvalid , getid , exitprog , validate_api
def test_isvalid():
    assert isvalid("this is not a url") == False
    assert isvalid("Google.com") == False
    assert isvalid("https://youtube.com") == False
    assert isvalid("youtube.com") == False
    assert isvalid("https://www.youtube.com/watch?v=fT2KhJ8W-Kg&list=WL&index=5&t=344s") == True
    assert isvalid("https://www.youtube.com/watch?v=fT2KhJ8W-Kg") == True
    assert isvalid("https://youtu.be/fT2KhJ8W-Kg") == True

def test_getid__format_youtube():
    assert getid("https://www.youtube.com/watch?v=fT2KhJ8W-Kg") == "fT2KhJ8W-Kg"
    assert getid("https://www.youtube.com/watch?v=LeSRHmKjNnM") == "LeSRHmKjNnM"

def test_getid__format_youtube_WL_T():
    assert getid("https://www.youtube.com/watch?v=6XYi5nSu_P0&list=WL&index=5&t=344s") == "6XYi5nSu_P0"
    assert getid("https://www.youtube.com/watch?v=gKgSvAyPFlU&list=WL&index=6") == "gKgSvAyPFlU"

def test_youtu_do_be():
    assert getid("https://youtu.be/fT2KhJ8W-Kg") == "fT2KhJ8W-Kg"
    assert getid("https://youtu.be/LeSRHmKjNnM") == "LeSRHmKjNnM"


def test_exitprog():
    with pytest.raises(SystemExit) as e:
        exitprog()
    assert e.type == SystemExit
    assert e.value.code == 0

def test_validate_api():
    with pytest.raises(SystemExit) as e:
        validate_api("") # no api key passed
    assert e.type == SystemExit
    assert e.value.code == 1
