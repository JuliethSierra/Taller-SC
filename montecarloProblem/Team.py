class Team:
    def __init__(self, name, players=None):
        self.name = name
        self.points = 0
        if players is None:
            self.players = []
        else:
            self.players = players

    def get_team_name(self):
        return self.name
    
    def set_team_name(self, name):
        self.name = name

    def get_team_points(self):
        return self.points
    
    def set_team_points(self, points):
        self.points = points
    
    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def get_players(self):
        return self.players

    def __str__(self):
        print("Team Name:", self.name)
        print("Team Points:", self.points)
        print("Players:")
        for player in self.players:
            print(player)



