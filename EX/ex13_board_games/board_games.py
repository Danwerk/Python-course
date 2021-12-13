"""Board game."""
from collections import Counter
from enum import Enum


class Statistics:
    """Game statistics."""

    def __init__(self, filename: str):
        """Constructor for Statistics class."""
        self.players = {}
        self.games = {}
        self.gameplays = []
        self.filename = filename
        self.read_file(filename)

    def read_file(self, filename):
        """Read data from file into dicts."""
        ret = []
        with open(filename, 'r') as f:
            f = f.readlines()
            for line in f:
                elements = line.split(';')
                game_name = elements[0]
                if game_name in self.games:
                    game = self.games[game_name]
                else:
                    game = Game(game_name)
                    self.games[game_name] = game_name
                #self.gameplays.append(GamePlay(name))

                players = elements[1].split(',')
                for name in players:
                    if name not in self.players:
                        player_obj = Player(name)
                        self.players[name] = player_obj
                # if elements[2] == 'points':
                #     self.game_has_points.append(game_str)
                # elif elements[2] == 'places':
                #     self.game_has_places.append(game_str)
                # elif elements[2] == 'winner':
                #     self.game_has_winner.append(game_str)

        ret.append(self.players)
        ret.append(self.games)
        return self.gameplays

    def get(self, path: str):
        """Basic getter."""
        tokens = path[1:].split('/')
        if tokens[0] == 'player':
            return self.functionality_get_player(path)
        if tokens[0] == 'game':
            return self.functionality_get_game(path)
        if path == '/players':
            return self.get_player_names()
        if path == '/games':
            return self.get_game_names()
    #     if path == '/total':
    #         return self.get_games_played_amount()
    #     if path == '/total/points' or path == '/total/places' or path == '/total/winner':
    #         return self.get_games_played_type(path)
    #
    def functionality_get_player(self, path):
        """Basic getter 2."""
        tokens = path[1:].split('/')
        player_name = tokens[1]
        player = self.players[player_name]
    #     if tokens[2] == 'amount':
    #         return player.get_games_played_count()
    #     elif tokens[2] == 'favourite':
    #         return player.get_games_played_most_by_player()
    #     elif tokens[2] == 'won':
    #         return player.get_games_won()
    #
    def functionality_get_game(self, path):
        """Basic getter 3."""
        tokens = path[1:].split('/')
        game_name = tokens[1]
        game = self.games[game_name]
        if tokens[2] == 'amount':
            return game.get_amount_of_played_games()
    #     elif tokens[2] == 'player-amount':
    #         pass

    def get_player_names(self) -> list:
        """Return list of players' names."""
        ret = []
        for player in self.players:
            ret.append(player)
        return ret

    def get_game_names(self) -> list:
        """List of games' names."""
        ret = []
        for game in self.games:
            ret.append(game)
        return ret


class GamePlayResultType(Enum):
    POINTS = 'points'
    WINNER = 'winner'
    PLACES = 'places'


class Game:
    """Game class."""

    def __init__(self, name):
        """Constructor for Game class."""
        self.name = name
        self.gameplays = []

    def __repr__(self):
        """Representation for Game."""
        return self.name

    def get_amount_of_played_games(self) -> int:
        pass


class GamePlay:
    """GamePlay class."""

    def __init__(self, game: Game):
        """GamePlay constructor."""
        self.game = game
        self.game_play_players = []
        self.result_type = None

    def new_gameplay(self):
        game_play = GamePlay(self)
        return game_play


class Player:
    """Game player."""

    def __init__(self, name):
        """Constructor for Player class."""
        self.name = name
        self.gameplays = []

    def __repr__(self):
        """Player representation."""
        return self.name

    def append_played_games(self, game: Game):
        """Add games person had played."""
        self.gameplays.append(game)

    def get_games_played_count(self):
        """Return amount of played games."""
        return len(self.gameplays)

    # def get_games_played_most_by_player(self) -> str:
    #     """Return most played games by player."""
    #     object_ret = []
    #     str_ret = []
    #     # make dict and find most played game by player.
    #     d = Counter(self.plays)
    #     most_elem = d[list(d.keys())[0]]
    #     for key, value in d.items():
    #         if value == most_elem:
    #             object_ret.append(key)
    #
    #     # object string representation
    #     for i in object_ret:
    #         str_ret.extend([key for (key, value) in self.games.items() if value == i])
    #     return str_ret[0]





if __name__ == '__main__':
    statistics = Statistics('ex13_input.txt')
    print(statistics.get('/players'))
    print(statistics.get('/games'))
    # print(statistics.get('/total'))
    #print(statistics.read_from_file('ex13_input.txt'))
    # print(statistics.get_player_names())
    # print(statistics.get_game_names())
    # print(statistics.total_played_games())
    # print(statistics.get_games_played_type('/total/points'))
    # print(statistics.get_games_played_type('/total/winner'))
    # print(statistics.get_games_played_type('/total/places'))
    # print(statistics.get('/player/joosep/amount'))
    # print(statistics.get('/player/ago/favourite'))
    # print(statistics.get('/player/ago/won'))
    # print(statistics.get_players_and_points_dict())
    # print(statistics.get('/game/chess/amount'))
