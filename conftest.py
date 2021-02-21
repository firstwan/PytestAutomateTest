import pytest
from pytest import fixture
# from config import Config
import json
import requests
from selenium import webdriver

#************************************
# Reffer: https://docs.pytest.org/en/stable/fixture.html
# Fixtures are created when first requested by a test, and are destroyed based on their scope:
#       function: the default scope, the fixture is destroyed at the end of the test.
#       class: the fixture is destroyed during teardown of the last test in the class.
#       module: the fixture is destroyed during teardown of the last test in the module.
#       package: the fixture is destroyed during teardown of the last test in the package.
#       session: the fixture is destroyed at the end of the test session.
#************************************

# addoption name can't change
def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store",
        help="Environment to run test case. And this is custom message"    
    )

    parser.addoption(
        "--user", 
        action="store",
        default="unittest",
        help="Login user id. Used to get token"    
    )

    parser.addoption(
        "--password", 
        action="store",
        default="asdf1234",
        help="Login user password. Used to get token"    
    )

@fixture(scope="session")
def env_fixture(request):
    return request.config.getoption("--env")

@fixture(scope="session")
def login_fixture(request):
    token = ""
    try:
        user_id = request.config.getoption("--user")
        password = request.config.getoption("--password")

        url = "https://backoffice-p5.foozxc.xyz/apiService/token"
        request_body = {
            "username": user_id,
            "password": password
        }
        response = requests.post(url, json=request_body)
        # pytest.fail("Failed on login")

        if response.status_code == 200:
            json_data = response.json()
            token = json_data["data"]["access_token"]
    except Exception:
        token = ""
    return token

# @fixture(scope="session")
# def app_config_fixture(env_fixture):
#     cfg = Config(env_fixture)
#     return cfg


@fixture(
    scope='session', 
    params=[webdriver.Chrome, webdriver.Edge]
    )
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


# def load_test_data(path):
#     with open(path) as data_file:
#         data = json.load(data_file)
#         return data
