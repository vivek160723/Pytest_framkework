import pytest


class TestClass:
    @pytest.fixture()
    def setup(self):
        print("Launching browser...")
        yield
        print("Closing browser")

    def testMethod1(self,setup):
        print("This is method one")

    def testMethod2(self,setup):
        print("This is method two")

    def testMethod3(self,setup):
        print("This is method Three")
