import pytest

def test_firstProgram():
    print("Hello")


#@pytest.mark.smoke
#@pytest.mark.skip
def test_Great():
    print("Good morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser)