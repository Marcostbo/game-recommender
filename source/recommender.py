from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


class Recommender:
    def __init__(self, game_data):
        self.game_data = game_data
        self.tfidf_matrix = None
        self.cosine_similarities = {}

    def create_tfidf_matrix(self):
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(self.game_data['summary'])
        self.tfidf_matrix = tfidf_matrix

    def create_cosine_similarities(self):
        cosine_similarities = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)
        for idx, row in self.game_data.iterrows():
            similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
            similar_items = [(cosine_similarities[idx][i], self.game_data['id'][i]) for i in similar_indices]
            self.cosine_similarities[row['id']] = similar_items[1:]

    def get_game_by_id(self, item_id):
        return self.game_data.loc[self.game_data['id'] == item_id]['name'].values[0]

    def recommend(self, item_id, number_of_recommendations):
        print("Recomendando " + str(number_of_recommendations)
              + " produtos simulares a " + self.get_game_by_id(item_id) + "...")
        print("-------")
        recs = self.cosine_similarities[item_id][:number_of_recommendations]
        for rec in recs:
            print(f"Recomendado: {self.get_game_by_id(rec[1])}")
