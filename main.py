from source.games import ReadGameFile
from source.recommender import Recommender

path = r'C:\Users\Marcos Oliveira\PycharmProjects\game_recommender\data\twitch_game_data.csv'
games = ReadGameFile()
games.read_data(path=path)

recommender = Recommender(game_data=games.data)
recommender.create_tfidf_matrix()
recommender.create_cosine_similarities()

desired_item_name = 'God of War'
desired_item_id = games.data.loc[games.data['name'] == desired_item_name]['id'].values[0]

recommender.get_game_by_id(desired_item_id)

recommender.recommend(
    item_id=desired_item_id,
    number_of_recommendations=10
)
