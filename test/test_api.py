# coding=utf-8
import json
import mock

from falcon import testing

from api_count.server import api as app


client = testing.TestClient(app)


@mock.patch('api_count.utils.request_url',
            mock.Mock(side_effect=("uelei",)))
def test_api():
    """
        Test request to api
    """
    response = client.simulate_get(
        query_string="url=http://blog.uelei.com&word=uelei").text

    assert json.loads(response) == {
        "url": "http://blog.uelei.com",
        "word": "uelei",
        "count": 1}

    response = client.simulate_get(
        query_string="url=http://blog.uelei.com").text

    assert json.loads(response) == {
        'description': 'The "word" parameter is required.',
        'title': 'Missing parameter'}

    response = client.simulate_get(
        query_string="word=brasil").text

    assert json.loads(response) == {
        'description': 'The "url" parameter is required.',
        'title': 'Missing parameter'}