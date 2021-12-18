"""Board game."""
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
                    self.read_file_2(players, points, gp)

                if elements[2] == 'places':
                    gp = game.new_gameplay('places')
                    places = elements[3].split(',')
                    places[-1] = places[-1].strip()
                    self.read_file_3(players, places,gp)

                if elements[2] == 'winner':
                    gp = game.new_gameplay('winner')
                    winner = elements[3].strip()
                    self.read_file_4(players, winner, gp)
                self.gameplays.append(gp)

        return self.gameplays


    def read_file_2(self, players, points, gp):
        for p in range(len(players)):
            if players[p] in self.players:
                player = self.players[players[p]]
            else:
                player = Player(players[p])
                self.players[players[p]] = player
            gp.add_player(player, int(points[p]))
            gp.get_gameplay_points_places_winner(player)
        return gp

    def read_file_3(self, players, places, gp):
        for p in range(len(players)):
            if places[p] in self.players:
                player = self.players[places[p]]
            else:
                player = Player(places[p])
                self.players[places[p]] = player
            gp.add_player(player, place=f'{p + 1}.place')
            gp.get_gameplay_points_places_winner(player)
        return gp

    def read_file_4(self, players, winner, gp):
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
        return gp

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
        if tokens[2] == 'record-holder':
            return game.get_game_record_holder()
        if tokens[2] == 'most-losses':
            return game.get_game_most_loser()
        if tokens[2] == 'most-frequent-loser':
            return game.get_most_frequent_loser()
        if tokens[2] == 'most-frequent-winner':
            return game.get_most_frequent_winner()

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


class Game:
    """Game class."""

    def __init__(self, name):
        """Constructor for Game class."""
        self.name = name
        self.gameplays = []
        self.most_wins = {}
        self.most_losses = {}

    def __repr__(self):
        """Representation for Game."""
        return self.name

    def get_amount_of_played_games(self) -> int:
        """Return how many games were played at all."""
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

    def get_game_most_wins(self) -> str:
        """Return player who won mostly."""
        ret = []
        win_amnt = 1
        for gp in self.gameplays:
            game_winner = gp.get_gameplay_winner()
            for i in range(len(game_winner)):
                if game_winner[i] not in self.most_wins:
                    self.most_wins[game_winner[i]] = win_amnt
                else:
                    self.most_wins[game_winner[i]] = win_amnt + 1
        max_winner_value = max(v for k, v in self.most_wins.items())

        for k, v in self.most_wins.items():
            if v == max_winner_value:
                ret.append(k.name)

        return ret[0]

    def get_game_record_holder(self) -> str:
        """Return the best player of some type of game."""
        # the highest score must be determined first.
        record = 0
        for game in self.gameplays:
            game_winner_points = game.get_gameplay_winner_points()
            if game_winner_points > record:
                record = game_winner_points
            else:
                continue
        # when we got the highest result then find the person who is the record holder.
        for gp in self.gameplays:
            gp_result = gp.get_score()
            for k, v in gp_result.items():
                if v == record:
                    return k.name

    def get_game_most_loser(self) -> str:
        """Return player(string) with the most losses in the game."""
        ret = []
        lose_amnt = 1
        for game in self.gameplays:
            game_loser = game.get_gameplay_loser()
            for i in range(len(game_loser)):
                if game_loser[i] not in self.most_losses:
                    self.most_losses[game_loser[i]] = lose_amnt
                else:
                    self.most_losses[game_loser[i]] = lose_amnt + 1
        max_loser_value = max(v for k, v in self.most_losses.items())

        for k, v in self.most_losses.items():
            if v == max_loser_value:
                ret.append(k.name)

        return ret[0]

    def get_most_frequent_winner(self) -> str:
        """Return the player's string with the highest percentage of wins."""
        frequency = {}
        self.get_game_most_wins()
        for k, v in self.most_wins.items():
            frequency[k.name] = v / len(self.gameplays)
        frequent_winner = min(k for k, v in frequency.items())
        return frequent_winner

    def get_most_frequent_loser(self) -> str:
        """Return the player's string with the highest percentage of losses."""
        frequency = {}
        self.get_game_most_loser()
        for k, v in self.most_losses.items():
            frequency[k.name] = v / len(self.gameplays)
        frequent_loser = min(k for k, v in frequency.items())
        return frequent_loser


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
        """Return player's favourite game that he/she played mostly."""
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
        """Return games player won."""
        ret = []
        count = 0
        for game in self.gameplays:
            wins = game.get_gameplay_winner()
            if self.name == wins[0].name:
                count += 1
            else:
                continue
            ret.append(wins)
        return count


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

    def get_score(self):
        """Getter for score dictionary."""
        return self.score

    def get_players(self):
        """Getter for gameplay players."""
        return self.game_play_players

    def get_gameplay_type(self):
        """Get gameplay type(e.g POINTS, WINNER, PLACES)."""
        return self.result_type

    def add_player(self, player: Player, points=None, place=None, winner=None):
        """Add player into new gameplay."""
        player.add_played_games(self)
        if points is not None:
            self.points = points
        if place is not None:
            self.place = place
        if winner is not None:
            self.winner = winner

        self.game_play_players.append(player)

    def get_gameplay_points_places_winner(self, player: Player):
        """Points/places/winner.

        Here we make a dictionary for each gameplay, where the key is the player and as a value is
        points/place/winner.
        """
        if self.result_type == GamePlayResultType.POINTS:
            self.score[player] = self.points
        if self.result_type == GamePlayResultType.PLACES:
            self.score[player] = self.place
        if self.result_type == GamePlayResultType.WINNER:
            self.score[player] = self.winner
        return self.score

    def get_gameplay_winner(self):
        """Return a player who won the gameplay."""
        if self.result_type == GamePlayResultType.POINTS:
            max_result = max(v for k, v in self.score.items())
            gp_winner = [k for k, v in self.score.items() if v == max_result]
            return gp_winner
        if self.result_type == GamePlayResultType.PLACES:
            gp_winner = [k for k, v in self.score.items() if v == '1.place']
            return gp_winner
        if self.result_type == GamePlayResultType.WINNER:
            gp_winner = [k for k, v in self.score.items() if v == 'winner']
            return gp_winner

    def get_gameplay_winner_points(self):
        """Return gameplay winner points only if game type is 'points'."""
        winner = self.get_gameplay_winner()
        winner_points = self.score[winner[0]]
        return winner_points

    def get_gameplay_loser(self):
        """Return a player who lost the gameplay."""
        if self.result_type == GamePlayResultType.POINTS:
            min_result = min(v for k, v in self.score.items())
            gp_loser = [k for k, v in self.score.items() if v == min_result]
            return gp_loser
        if self.result_type == GamePlayResultType.PLACES:
            gp_loser = [k for k, v in self.score.items() if v == f'{len(self.score)}.place']
            return gp_loser


if __name__ == '__main__':
    statistics = Statistics('ex13_input.txt')
    # print(statistics.read_file('ex13_input.txt'))
    # print(statistics.get('/players'))
    # print(statistics.get('/games'))
    # print(statistics.get('/total'))  # 5
    print(statistics.get('/total/points'))  # 3
    print(statistics.get('/total/winner'))  # 1
    print(statistics.get('/total/places'))  # 1
    # print(statistics.get('/player/kristjan/amount'))  # 3
    # print(statistics.get('/player/kristjan/favourite'))  # 7 wonders
    # print(statistics.get('/player/joosep/won'))
    # print(statistics.get('/game/terraforming mars/amount'))  # 2
    # print(statistics.get('/game/terraforming mars/player-amount'))
    # print(statistics.get('/game/terraforming mars/most-wins'))
    # print(statistics.get('/game/7 wonders/record-holder'))
    # print(statistics.get('/game/chess/most-losses'))
    # print(statistics.get('/game/terraforming mars/most-frequent-loser'))
    # print(statistics.get('/game/terraforming mars/most-frequent-winner'))
