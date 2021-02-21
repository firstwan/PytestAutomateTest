import requests
import json
import pytest
from pytest import mark


@mark.payment
def test_get_merchant_as_expected(login_fixture):
    url = "https://backoffice-p5.foozxc.xyzaaa/epsService/Merchants"
    response_data = {}
    token = login_fixture

    response = requests.get(
        url, headers={'Authorization': "Bearer %s" % token})

    response_data = response.json()

    # Print the message out if test failed
    print(response_data["code"])
    print(response_data["message"])

    assert response.status_code == 200
    assert response_data["success"]
    assert int(response_data["code"]) == 0


@mark.test
def test_feature():
    assert True
