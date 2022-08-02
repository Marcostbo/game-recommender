import pandas as pd


class ReadGameFile:
    def __init__(self):
        self.path = None
        self.data = None
        self.number_of_games = None

    def read_data(self, path):
        self.path = path
        games = pd.read_csv(self.path)
        games = games.drop(columns='Unnamed: 0')
        self.data = games
        self.number_of_games = len(games)
