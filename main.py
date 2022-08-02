from source.games import ReadGameFile
from source.recommender import Recommender
import time


# STEP 1: Read file data
start_time = time.time()

path = r'C:\Users\Marcos Oliveira\PycharmProjects\game_recommender\data\twitch_game_data.csv'
games = ReadGameFile()
games.read_data(path=path)

final_time = time.time()
file_elapsed_time = final_time - start_time

# STEP 2: Recommendations
start_time = time.time()

recommender = Recommender(game_data=games.data)
recommender.create_tfidf_matrix()
recommender.create_cosine_similarities()

desired_item_name = 'God of War'
desired_item_id = games.data.loc[games.data['name'] == desired_item_name]['id'].values[0]

recommender.recommend(
    item_id=desired_item_id,
    number_of_recommendations=10
)

final_time = time.time()
recommendation_elapsed_time = final_time - start_time
