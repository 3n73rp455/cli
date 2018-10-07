import requests


def password(token, pk):
    headers = {'Authorization': 'JWT {0}'.format(token)}
    url = 'http://localhost:8000/api/v1/passwords/{0}/'.format(pk)
    r = requests.get(url, headers=headers)
    data = r.json()
    pw = data['password']
    return pw