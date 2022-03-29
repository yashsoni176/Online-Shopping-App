import pytest

@pytest.fixture(scope="session",autouse=True)
def setUp():
    print("Open Amazon App")
    print("User logged In")
    yield
    print("User Logged Out")
    print("Closed Amazon App")
