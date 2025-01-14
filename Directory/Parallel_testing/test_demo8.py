import pytest

class TestCase:
    @pytest.mark.parametrize("num1,num2",[(10,10),(2,3),(2,2),(3,4)])
    def test_calculate(self,num1,num2):
        assert num1==num2