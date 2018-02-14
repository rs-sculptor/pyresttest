import requests
import pyresttest.validators as validators

"""

inspired by: https://openedx.atlassian.net/wiki/spaces/TE/pages/69501046/Discovery+Automated+testing+of+API+endpoints

Usage:

- config:
    - testset: "Course Discovery API tests"
    - generators:
        - 'token': {type: 'token', url: 'http://localhost:8001/tokens/', uid: 'admin', passwd: 'admin', field: 'encoded'}
- test:
    - generator_binds: {token: token}
    - name: "Get a list of Catalogs"
    - url: "/api/v1/catalogs/"
    - method: "GET"
    - headers: {template: {'Authorization': 'Bearer $token', 'Content-Type': 'application/json'}}
    - expected_status: [200]
    - validators:
        - compare: {jsonpath_mini: "count", comparator: "eq", expected: 0}
"""
def token(config):
    def get_token(url, uid, passwd, field):
        """Get a bearer token and return its value. """
        session = requests.Session()
        params = {
            'uid': uid,
            'passwd': passwd,
        }
        response = session.post(url, params=params)
        if not response.ok:
            print(response.status_code)
            raise ValueError("An error occurred: {}".format(response.text))

        resp = response.json()
        token = resp[field] if field else resp
        yield token

    token = get_token(
        url=config.get('url'),
        uid=config.get('uid', ''),
        passwd=config.get('passwd', ''),
        field=config.get('field', ''),
    )
    return token


GENERATORS = {'token': token}