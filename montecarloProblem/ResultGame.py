from montecarloProblem.Team import Team
from montecarloProblem.player import Player


class ResultGame: 

    def __init__(
            self, 
            firstTeam: Team, 
            secondTeam:Team, 
            winnerTeam: Team, 
            moreLuckyPlayer: Player,
            moreExperiencePlayer: Player,
            genderMoreWinnerEachGame: Player,
            genderMoreWinnerTotal: Player
        ):
        self.firstTeam: Team = firstTeam
        self.secondTeam: Team = secondTeam

        self.winnerTeam: Team = winnerTeam
        self.moreLuckyPlayer: Player = moreLuckyPlayer
        self.moreExperiencePlayer: Player = moreExperiencePlayer
        self.genderMoreWinnerEachGame: Player = genderMoreWinnerEachGame
        self.genderMoreWinnerTotal: Player = genderMoreWinnerTotal

  # Setters
    def set_winner_team(self, winner_team: Team):
        self.winnerTeam = winner_team

    def set_more_lucky_player(self, player: Player):
        self.moreLuckyPlayer = player

    def set_more_experience_player(self, player: Player):
        self.moreExperiencePlayer = player

    def set_gender_more_winner_each_game(self, player: Player):
        self.genderMoreWinnerEachGame = player

    def set_gender_more_winner_total(self, player: Player):
        self.genderMoreWinnerTotal = player

    # Getters
    def get_first_team(self) -> Team:
        return self.firstTeam    

    def get_second_team(self) -> Team:
        return self.secondTeam   
       
    def get_winner_team(self) -> Team:
        return self.winnerTeam

    def get_more_lucky_player(self) -> Player:
        return self.moreLuckyPlayer

    def get_more_experience_player(self) -> Player:
        return self.moreExperiencePlayer

    def get_gender_more_winner_each_game(self) -> Player:
        return self.genderMoreWinnerEachGame

    def get_gender_more_winner_total(self) -> Player:
        return self.genderMoreWinnerTotal

    # __str__ method
    def __str__(self):
        return f"Match between {self.firstTeam.__str__()} and {self.secondTeam.__str__()}.\nWinner: {self.winnerTeam.__str__() if self.winnerTeam else 'Not decided yet'}.\nPoints: FirstTeam {self.firstTeam.get_team_points()} - SecondTeam {self.secondTeam.get_team_points()}.\nMore Lucky Player: {self.moreLuckyPlayer.__str__() if self.moreLuckyPlayer else 'None'}.\n(¿?) More Experienced Player: {self.moreExperiencePlayer.__str__() if self.moreExperiencePlayer else 'None'}.\nGender More Winner Each Game: {self.genderMoreWinnerEachGame.__str__() if self.get_gender_more_winner_each_game() else 'None'}.\nGender More Winner Total: {self.genderMoreWinnerTotal.__str__() if self.genderMoreWinnerTotal else 'None'}"
