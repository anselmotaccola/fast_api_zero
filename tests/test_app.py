from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        'users/',
        json={
            'username': 'testeusername',
            'password': '123456',
            'email': 'teste@teste.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testeusername',
                'email': 'teste@teste.com',
                'id': 1,
            }
        ]
    }


def test_read_users_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testeusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'password': '',
            'username': 'updateusername',
            'email': 'teste@teste.com',
            'id': 1,
        },
    )

    assert response.json() == {
        'username': 'updateusername',
        'email': 'teste@teste.com',
        'id': 1,
    }


def test_update_user_status_code(client):
    response = client.put(
        '/users/1',
        json={
            'password': '',
            'username': 'updateusername',
            'email': 'teste@teste.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK


def test_update_user_status_code_Not_Found(client):
    response = client.put(
        '/users/20',
        json={
            'password': '',
            'username': 'updateusername',
            'email': 'teste@teste.com',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}


def test_delete_user_NOT_Found(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_read_users_id_NOT_Found(client):
    response = client.get('/users/1000')

    assert response.status_code == HTTPStatus.NOT_FOUND
