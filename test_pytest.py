import pytest
from main import isvalid , getid

def test_isvalid():
    assert isvalid("this is not a url") == False
    assert isvalid("Google.com") == False
    assert isvalid("https://youtube.com") == False
    assert isvalid("youtube.com") == False
    assert isvalid("https://www.youtube.com/watch?v=6XYi5nSu_P0&list=WL&index=5&t=344s") == True
    assert isvalid("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == True

def test_getid():
    ...