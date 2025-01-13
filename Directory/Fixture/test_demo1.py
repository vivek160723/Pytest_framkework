import pytest


class TestClass:
    def testMethod1(self,setup):
        print("This is method one")

    def testMethod2(self,setup):
        print("This is method two")

    @pytest.mark.skip
    def testMethod3(self,setup):
        print("This is method Three")
