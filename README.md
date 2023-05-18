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

Através da documentação da Twitch API, podemos fazer a requisição das informações necessárias, bem como aplicar filtros para selecionar jogos com características específicas.Será retornado: Nome, Categoria, Data e Resumo para os jogos lançados após 2014 para PS4 (Código 48) ou XONE (Código 49). A instância da classe IGBDWrapper acessa a API para o endpoint desejado.

Para mais informações a respeito dos dados e filtros disponíveis, acesse a documentação da API em https://api-docs.igdb.com/#about

```
wrapper = IGDBWrapper(headers['Client-ID'], keys['access_token'])

def get_game_data(page, page_elements):
    byte_array = wrapper.api_request(
                'games',
                f'fields name, category, first_release_date, summary; offset {page*page_elements}; \
                limit {page_elements}; where (release_dates.platform = (48, 49) & release_dates.y >= 2014);;'
              )
    game_data = byte_array.json()
    return game_data


```
