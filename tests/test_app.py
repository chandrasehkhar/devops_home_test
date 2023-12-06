import json


def test_index(app, client):
    del app
    res = client.get('/hello')
    assert res.status_code == 200
  
