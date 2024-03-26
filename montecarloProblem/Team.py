class Team:
    def __init__(self, name, players=None):
        self.name = name
        if players is None:
            self.players = []
        else:
            self.players = players

    def get_team_name(self):
        return self.name
    
    def set_team_name(self, name):
        self.name = name
    
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    #def __str__(self):
    #   player_names = ", ".join([player.player_id for player in self.players])
    #    return f"Team: {self.name}, Players: {player_names}"
    def __str__(self):
        player_details = "\n".join([f"Player ID: {player.player_id}, Gender: {player.get_gender()}, Endurance: {player.get_endurance()}, Experience: {player.get_experience()}, Luck: {player.get_luck()}" for player in self.players])
        return f"Team: {self.name}\nPlayers:\n{player_details}"



