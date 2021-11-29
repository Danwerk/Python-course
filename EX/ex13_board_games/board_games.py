class Statistics:
    """Game statistics."""

    def __init__(self, filename: str):
        """Constructor for Statistics class."""
        self.players = {}
        self.games = {}
        self.game_has_points = []
        self.game_has_places = []
        self.game_has_winner = []
        self.games_played_count = sum(1 for line in open(filename))
        self.filename = self.read_from_file(filename)

    def get_file_data(self):
        """Getter for read from file func."""
        return self.filename

    def get_players(self):
        """Players' dict getter."""
        return self.players

    def get_games(self):
        """Games dict getter."""
        return self.games

    def read_from_file(self, filename='ex13_input.txt'):
        """Read data from file into dicts."""
        ret = []
        with open(filename, 'r') as f:
            f = f.readlines()
            for line in f:
                elements = line.split(';')
                game_obj = Game(elements[0])
                game_str = elements[0]

                #  add games into dictionary where the key is the name of a game and the value is a game object
                if game_str not in self.games:
                    self.games[game_str] = game_obj
                #  devide games into groups of different types of games.
                people = elements[1].split(',')

                if elements[2] == 'points':
                    self.game_has_points.append(game_str)
                elif elements[2] == 'places':
                    self.game_has_places.append(elements[0])
                elif elements[2] == 'winner':
                    self.game_has_winner.append(elements[0])


                for player in people:
                    player_obj = Player(player)
                    if player not in self.players:
                        self.players[player] = player_obj

        ret.append(self.players)
        ret.append(self.games)
        print(self.game_has_points)
        return ret

    def get(self, path: str):
        """Basic getter."""
        tokens = path[1:].split('/')
        if path == '/players':
            return self.get_player_names()
        if path == '/games':
            return self.get_game_names()
        if path == '/total':
            return self.get_games_played_amount()
        if path == '/total/points' or path == '/total/places' or path == '/total/winner':
            return self.get_games_played_type(path)


    def get_player_names(self) -> list:
        """List of players' names."""
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
        if path == '/total/points':
            return len(self.game_has_points)
        elif path == '/total/places':
            return len(self.game_has_places)
        elif path == '/total/winner':
            return len(self.game_has_winner)


class Game:
    def __init__(self, name):
        """Constructor for Game class."""
        self.name = name


class Player:
    def __init__(self, name):
        """Constructor for Player class."""
        self.name = name

    def __repr__(self):
        """Player representation."""
        return self.name


if __name__ == '__main__':
    statistics = Statistics('ex13_input.txt')
    # player = Player('Ago')
    #print(statistics.get('/players'))
    #print(statistics.get('/total'))
    #print(statistics.get('/games'))
    #print(statistics.read_from_file('ex13_input.txt'))
    # print(statistics.get_player_names())
    # print(statistics.get_game_names())
    # print(statistics.total_played_games())
    print(statistics.get_games_played_type('/total/points'))
    print(statistics.get_games_played_type('/total/winner'))
    print(statistics.get_games_played_type('/total/places'))
