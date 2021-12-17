"""Board game."""
from collections import Counter
from enum import Enum


class GamePlayResultType(Enum):
    """GamePlayResultType class."""
    POINTS = 'points'
    WINNER = 'winner'
    PLACES = 'places'


class Statistics:
    """Game statistics."""

    def __init__(self, filename: str):
        """Constructor for Statistics class."""
        self.filename = filename
        self.players = {}
        self.games = {}
        self.gameplays = []
        self.read_file(filename)

    def __repr__(self):
        """Represention for Statistics class."""
        return f'{self.gameplays}'

    def read_file(self, filename):
        """Read data from file into dicts."""
        ret = []
        with open(filename, 'r') as f:
            f = f.readlines()
            for line in f:
                elements = line.split(';')
                game_name = elements[0]
                players = elements[1].split(',')

                if game_name in self.games:
                    game = self.games[game_name]
                else:
                    game = Game(game_name)
                    self.games[game_name] = game

                if elements[2] == 'points':
                    points = elements[3].split(',')
                    points[-1] = points[-1].strip()
                    gp = game.new_gameplay('points')
                    for p in range(len(players)):
                        if players[p] in self.players:
                            player = self.players[players[p]]
                        else:
                            player = Player(players[p])
                            self.players[players[p]] = player
                        gp.add_player(player, int(points[p]))
                        gp.get_gameplay_points_places_winner(player)

                if elements[2] == 'places':
                    gp = game.new_gameplay('places')
                    places = elements[3].split(',')
                    places[-1] = places[-1].strip()
                    for p in range(len(players)):
                        if players[p] in self.players:
                            player = self.players[players[p]]
                        else:
                            player = Player(players[p])
                            self.players[players[p]] = player
                        gp.add_player(player, place=f'{p + 1}.place')
                        gp.get_gameplay_points_places_winner(player)

                if elements[2] == 'winner':
                    gp = game.new_gameplay('winner')
                    winner = elements[3].strip()
                    for p in range(len(players)):
                        if players[p] in self.players:
                            player = self.players[players[p]]
                        else:
                            player = Player(players[p])
                            self.players[players[p]] = player
                        if players[p] != winner:
                            gp.add_player(player, winner='loser')
                            gp.get_gameplay_points_places_winner(player)
                        else:
                            gp.add_player(player, winner='winner')
                            gp.get_gameplay_points_places_winner(self.players[winner])

                self.gameplays.append(gp)

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
        if path == '/total':
            return len(self.gameplays)
        if path == '/total/points':
            return self.get_games_played_type_count('points')
        if path == '/total/places':
            return self.get_games_played_type_count('places')
        if path == '/total/winner':
            return self.get_games_played_type_count('winner')

    def functionality_get_player(self, path):
        """Basic getter 2."""
        tokens = path[1:].split('/')
        player_name = tokens[1]
        player = self.players[player_name]

        if tokens[2] == 'amount':
            return player.get_games_played_count()
        if tokens[2] == 'favourite':
            return player.get_favourite_game()
        if tokens[2] == 'won':
            return player.get_games_won()

    def functionality_get_game(self, path):
        """Basic getter 3."""
        tokens = path[1:].split('/')
        game_name = tokens[1]
        game = self.games[game_name]
        if tokens[2] == 'amount':
            return game.get_amount_of_played_games()
        if tokens[2] == 'player-amount':
            return game.get_game_player_amount()
        if tokens[2] == 'most-wins':
            return game.get_game_most_wins()

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

    def get_games_played_type_count(self, game_type: str):
        """Return count of specific type of game has been played."""
        count = 0
        for i in self.gameplays:
            if i.get_gameplay_type() == GamePlayResultType(game_type):
                count += 1
        return count

    def get_points_winner_places(self):
        pass


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
        return len(self.gameplays)

    def new_gameplay(self, game_type: str):
        """Create and add new GamePlay object into list."""
        game_play = GamePlay(self, game_type)
        self.gameplays.append(game_play)
        return game_play

    def get_game_player_amount(self) -> int:
        """Return amount of players that played most often the game."""
        ret = []
        for g in self.gameplays:
            ret.append(g.game_play_players)
        return max(len(elem) for elem in ret)

    def get_game_most_wins(self):
        for game in self.gameplays:
            game.get_gameplay_winner()


class Player:
    """Game player."""

    def __init__(self, name):
        """Constructor for Player class."""
        self.name = name
        self.gameplays = []

    def __repr__(self):
        """Player representation."""
        return f'{self.name}'

    def add_played_games(self, gameplay: 'GamePlay'):
        """Add games person had played/gameplay(s) in which a player has taken part."""
        self.gameplays.append(gameplay)

    def get_games_played_count(self):
        """Return amount of played games."""
        return len(self.gameplays)

    def get_favourite_game(self) -> str:
        """Return favourite game."""
        ret = {}
        count = 1
        for game in self.gameplays:
            if game.game not in ret:
                ret[game.game] = count
            else:
                ret[game.game] = count + 1
        max_value = max([v for k, v in ret.items()])
        max_elem = [k for k, v in ret.items() if v == max_value]

        for g in max_elem:
            return g.name

    def get_games_won(self):
        ret = []
        for game in self.gameplays:
            wins = game.get_gameplay_points_places_winner(self)
            ret.append(wins)
        return ret


class GamePlay:
    """GamePlay class."""

    def __init__(self, game: Game, game_type: str):
        """GamePlay constructor."""
        self.game = game
        self.game_play_players = []
        self.result_type = GamePlayResultType(game_type)
        self.points = None
        self.place = None
        self.winner = None
        self.score = {}

    def __repr__(self):
        """Representation for GamePlay class."""
        return f'{self.result_type} result:{self.score}///'

    def add_player(self, player: Player, points=None, place=None, winner=None):
        """..."""
        player.add_played_games(self)
        if points is not None:
            self.points = points
        if place is not None:
            self.place = place
        if winner is not None:
            self.winner = winner

        self.game_play_players.append(player)

    def get_gameplay_points_places_winner(self, player: Player):
        if self.result_type == GamePlayResultType.POINTS:
            self.score[player] = self.points
        if self.result_type == GamePlayResultType.PLACES:
            self.score[player] = self.place
        if self.result_type == GamePlayResultType.WINNER:
            self.score[player] = self.winner
        return self.score

    def get_gameplay_winner(self):
        """..."""
        if self.result_type == GamePlayResultType.POINTS:
            print(self.game_play_players)
            return max(v for k, v in self.score.items())

    def get_players(self):
        """Getter for gameplay players."""
        return self.game_play_players

    def get_gameplay_type(self):
        """Get gameplay type(e.g POINTS, WINNER, PLACES)."""
        return self.result_type

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
    # print(statistics.read_file('ex13_input.txt'))
    # print(statistics.get('/players'))
    # print(statistics.get('/games'))
    # print(statistics.get('/total'))
    # print(statistics.get('/total/points'))
    # print(statistics.get('/total/winner'))
    # print(statistics.get('/total/places'))
    # print(statistics.get('/player/kristjan/amount'))
    # print(statistics.get('/player/kristjan/favourite'))
    # print(statistics.get('/player/kristjan/won'))
    # print(statistics.get('/game/7 wonders/amount'))
    # print(statistics.get('/game/terraforming mars/player-amount'))
    print(statistics.get('/game/terraforming mars/most-wins'))

    # gp = GamePlay(Game('chess'), 'points')
    # gp.add_player(Player('ago'))
    # print(gp.get_players())

    # print(statistics.get_players_and_points_dict())
