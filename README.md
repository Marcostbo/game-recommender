# Game recommender (Database via Twitch API)

Como consumir a API da Twitch para obter os dados?

![image](https://user-images.githubusercontent.com/42622686/133302352-393faabc-fe5d-46ee-ae0a-a42f9aaacc52.png)

Primeiramente, deve-se obter as chaves de acesso para o seu perfil na Twitch Developers. Após isso, através da biblioteca de Requests, pode-se obter seu token de acesso, o qual é necessário para acessar a database

```
import requests
client_id = client_id
client_secret = client_secret

body = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

r = requests.post('https://id.twitch.tv/oauth2/token', body)
```
Agora é possivel criar o dicionário headers para acesso na API.

```
keys = r.json()

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

app_token = headers['Authorization']
```
A classe IGBDWrapper acessa a API para o endpoint desejado

```
from requests import post
from requests.models import Request, Response

API_URL = "https://api.igdb.com/v4/"

class IGDBWrapper:
    def __init__(self, client_id:str, auth_token:str) -> None:
        self.client_id = client_id
        self.auth_token = auth_token

    def api_request(self, endpoint:str, query:str) -> Response:
        """
        Recebe um endpoint e a APIcalypse query e retorna a resposta API.
        """
        url = IGDBWrapper._build_url(endpoint)
        params = self._compose_request(query)

        response = post(url, **params)
        response.raise_for_status()

        return response

    @staticmethod
    def _build_url(endpoint:str='') -> str:
        return ('%s%s' % (API_URL, endpoint))

    def _compose_request(self, query:str) -> Request:
       
        request_params = {
            'headers': {
                'Client-ID': self.client_id,
                'Authorization': ('Bearer %s' % (self.auth_token)),
            }
        }

        if isinstance(query, str):
            request_params['data'] = query
            return request_params
```
