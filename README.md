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
