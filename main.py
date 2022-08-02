from source.games import ReadGameFile

path = r'C:\Users\Marcos Oliveira\PycharmProjects\game_recommender\data\twitch_game_data.csv'
games = ReadGameFile()
games.read_data(path=path)
