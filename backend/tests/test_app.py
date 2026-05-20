import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import app as flask_app

def test_home():

    client = flask_app.app.test_client()

    r = client.get('/')

    assert r.status_code == 200

def test_health():

    client = flask_app.app.test_client()

    r = client.get('/health')

    assert r.status_code == 200

def test_db():

    client = flask_app.app.test_client()

    r = client.get('/db')

    assert r.status_code == 200
