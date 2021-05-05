import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be execute first")
    yield
    print("i will be execute last")


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["vinay", "kumar", "rahulshettyacademic.com"]


@pytest.fixture(params=[("chrome", "vinay"), ("firefox", "kumar"), ("IE", "ray")])
def crossBrowser(request):
    return request.param
