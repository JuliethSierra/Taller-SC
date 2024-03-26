class Player:
    def __init__(self, player_id, gender, endurance, luck):
        self.player_id = player_id
        self.gender = gender
        self.endurance = endurance
        self.experience = 10
        self.luck = luck
        self.points = 0
        self.enduranceRound = endurance
        self.roundWin = 0
        self.roundDiscount = 0

    def get_player_id(self):
        return self.player_id

    def get_gender(self):
        return self.gender

    def get_endurance(self):
        return self.endurance

    def get_experience(self):
        return self.experience

    def get_luck(self):
        return self.luck

    def get_points(self):
        return self.points

    def get_endurance_round(self):
        return self.enduranceRound

    def get_round_win(self):
        return self.roundWin
    
    def get_round_discount(self):
        return self.roundDiscount
    
    def set_player_id(self, player_id):
        self.player_id = player_id

    def set_gender(self, gender):
        self.gender = gender

    def set_endurance(self, endurance):
        self.endurance = endurance

    def set_experience(self, experience):
        self.experience = experience

    def set_luck(self, luck):
        self.luck = luck

    def set_points(self, points):
        self.points = points

    def set_enduranceRound(self, enduranceRound):
        self.enduranceRound = enduranceRound

    def set_roundWin(self, roundWin):
        self.roundWin = roundWin

    def set_roundDiscount(self, roundDiscount):
        self.roundDiscount = roundDiscount

    def __str__(self):
        return f"Player ID: {self.player_id}, Gender: {self.gender}, endurance:{self.endurance}, enduranceRound:{self.get_endurance_round()}, Luck: {self.luck}, roundWin: {self.get_round_win()},  experience: {self.get_experience()}, points: {self.get_points()}"

