"""Board game."""
from collections import Counter


class Statistics:
    """Game statistics."""

    def __init__(self, filename: str):
        """Constructor for Statistics class."""
        self.players = []
        self.games = []
        self.games_player_had_played = {}
        self.players_objects = {}
        self.games_objects = {}
        self.gameplays = []
        self.filename = self.read_from_file(filename)


    def read_from_file(self, filename):
        """Read data from file into dicts."""
        ret = []
        with open(filename, 'r') as f:
            f = f.readlines()
            for line in f:
                elements = line.split(';')
                self.gameplays.append(GamePlay(elements, self.players, self.games))

                people = elements[1].split(',')
                for name in people:
                    if name not in self.players_objects:
                        player_obj = Player(name)
                        self.players_objects[name] = player_obj
                        self.players.append(name)
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
    #     if path == '/games':
    #         return self.get_game_names()
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

    def get_games_played_amount(self) -> int:
        """Total amount of played games."""
        return self.games_played_count

    def get_games_played_type(self, path) -> int:
        """Calculate for each game type, how many times this game was played."""
        if path == '/total/points':
            return len(self.game_has_points)
        elif path == '/total/places':
            return len(self.game_has_places)
        elif path == '/total/winner':
            return len(self.game_has_winner)


class Game:
    """Game class."""

    def __init__(self, game_name, games: dict, names: dict, gameplays):
        """Constructor for Game class."""
        self.game_name = game_name

    def __repr__(self):
        """Representation for Game."""
        return self.game_name

    def get_amount_of_played_games(self) -> int:
        pass



class GamePlay:
    """GamePlay class."""

    def __init__(self, gameplays: list, players, games):
        """GamePlay constructor."""
        self.gameplays = gameplays
        self.players = players
        self.games = games
        self.winner = []

    def get_gameplays(self):
        return self.gameplays

    def get_winner(self):
        """Get winner of gameplay."""
        d = {}
        people = self.gameplays[1].split(',')
        if self.gameplays[2] == 'points':
            points = self.gameplays[3].split(',')
            points[-1] = points[-1].strip()
            for i in range(len(points)):
                d[self.players[people[i]]] = int(points[i])
            winner = max(d, key=d.get)
            return winner

        elif self.gameplays[2] == 'places':
            places = self.gameplays[3].split(',')
            places[-1] = places[-1].strip()
            winner = self.players[places[0]]
            return winner

        elif self.gameplays[2] == 'winner':
            game_player = self.gameplays[3].split(',')
            game_player[0] = game_player[0].strip()
            return self.players[game_player[0]]


class Player:
    """Game player."""

    def __init__(self, name):
        """Constructor for Player class."""
        self.name = name
        self.plays = []

    def __repr__(self):
        """Player representation."""
        return self.name

    def append_played_games(self, game: Game):
        """Add games person had played."""
        self.plays.append(game)

    def get_games_played_count(self):
        """Return amount of played games."""
        return len(self.plays)

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

    '''
if len(str_ret) > 0:
    joined_string = ", ".join(str_ret)
        return f'{joined_string}'
'''



if __name__ == '__main__':
    statistics = Statistics('ex13_input.txt')
    # player = Player('Ago')
    print(statistics.get('/players'))
    # print(statistics.get('/total'))
    # print(statistics.get('/games'))
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
