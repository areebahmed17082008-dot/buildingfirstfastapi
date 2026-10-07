from main import app


def test_get_user():
    client = app.test_client()
    response = client.get('/get-user/42?extra=yes')
    assert response.status_code == 200
    data = response.get_json()
    assert data['user_id'] == '42'
    assert data['extra'] == 'yes'


def test_create_user_valid_json():
    client = app.test_client()
    response = client.post('/create-user', json={'name': 'Alice'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'Alice'


def test_create_user_invalid_json():
    client = app.test_client()
    response = client.post('/create-user', data='not-json', content_type='application/json')
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Request body must be valid JSON'
