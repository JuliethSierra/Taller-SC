class Team:
    def __init__(self, name, players=None):
        self.name = name
        if players is None:
            self.players = []
        else:
            self.players = players

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def __str__(self):
        player_names = ", ".join([player.player_id for player in self.players])
        return f"Team: {self.name}, Players: {player_names}"



