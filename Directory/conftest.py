import pytest


@pytest.fixture()
def setup():
    print("Launching browser...")
    yield
    print("Closing browser")