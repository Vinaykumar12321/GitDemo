import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture(self):
        print("i will be execute in fixture demo")

    def test_fixture1(self):
        print("i will be execute in fixture1 demo")

    def test_fixture2(self):
        print("i will be execute in fixture2 demo")

    def test_fixtur3(self):
         print("i will be execute in fixture3 demo")
