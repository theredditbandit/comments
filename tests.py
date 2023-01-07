import pytest
from main import isvalid


def test_isvalid():
    assert isvalid("this is not a url") == False
    assert isvalid("Google.com") == False
    assert isvalid("https://youtube.com") == True
    assert isvalid("youtube.com") == True
    assert isvalid("https://www.youtube.com/watch?v=6XYi5nSu_P0&list=WL&index=5&t=344s") == True
