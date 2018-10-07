import requests

headers = {'Content-Type': 'application/json'}


def login(user, password):
    payload = {'username': user, 'password': password}
    r = requests.post('http://localhost:8000/auth/login/', json=payload, headers=headers)
    data = r.json()
    token = data['token']
    return token