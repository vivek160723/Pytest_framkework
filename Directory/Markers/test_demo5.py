import pytest

class TestExample5:

    @pytest.mark.sanity
    def test_alpha(self):
        assert True

    @pytest.mark.sanity
    def test_gamma(self):
        assert False

    @pytest.mark.Regression
    def test_beta(self):
        assert True