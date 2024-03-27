import random
from montecarloProblem.ResultGame import ResultGame
from montecarloProblem.Team import Team
from montecarloProblem.player import Player

class Game:
    firstTeamFinalScore = 0
    secondTeamFinalScore = 0
    consecutiveLaunches = 3
    originalExperience = 10
    accumulatedExperience = 9
    roundDiscount = 0

    def create_player(self, id, gender, endurance, luck):
        return Player(id, "female" if gender == 1 else "male", endurance, (float(1 + (3 - 1) *luck)))

    def create_teams(self, name):
        players = []
        for i in range(5):
            player = self.create_player((name + "_" + str(i)), random.randint(0, 1), random.randint(10, 35), random.random())
            players.append(player)
        team = Team(name=name, players=players)
        return team

    
    def launch(self, player):
            if player.gender == 'female':
                precision = [0.3, 0.68, 0.95, 1.0]  # Probabilidades acumuladas para las categorías de precisión
                scores = [10, 9, 8, 0]            # Puntajes correspondientes a cada categoría de precisión
            else:
                precision = [0.2, 0.55, 0.95, 1.0]   # Probabilidades acumuladas para las categorías de precisión
                scores = [10, 9, 8, 0]            # Puntajes correspondientes a cada categoría de precisión

            # Generamos un número aleatorio entre 0 y 1 para determinar la categoría de precisión
            random_number = random.random()
            for i in range(len(precision)):
                if random_number <= precision[i]:
                    score = scores[i]
                    break
            return score
    
    def discountEndurance(self,player:Player):
        points = 0
        endurance = player.get_endurance()

        if endurance >= 5:
            player.set_total_rounds(player.get_total_rounds() + 1)

        while endurance >= 5:
            points += self.launch(player)
            endurance -= 5
            player.set_points(points)
        
        return points

    def calculateEnduranceRound(self, player):
        endurance = player.get_endurance_round()
        if endurance > 5:
            enduranceRound = 0
            if(player.get_experience() > (self.originalExperience + self.accumulatedExperience)):
                self.calculateDiscountRoundsendurence(player, endurance)
            else:
                enduranceRound = endurance - int(random.randint(1, 2))
                player.set_enduranceRound(enduranceRound)
            return enduranceRound
    
    def calculateDiscountRoundsendurence(self, player, endurance):
        roundAmount = player.get_round_discount() + 1
        player.set_roundDiscount(roundAmount)
        if roundAmount <= self.roundDiscount:
            enduranceRound = endurance - 1
            player.set_enduranceRound(enduranceRound)
            return enduranceRound
        else:
            enduranceRound = endurance - int(random.randint(1, 2))
            player.set_enduranceRound(enduranceRound)
            return enduranceRound

    def generateLuck(self, player: Player):
        if player.get_endurance() >= 5:
            lucky = random.uniform(1, 3)
            player.set_total_lucky(player.get_total_lucky() + lucky)
            player.set_luck(lucky)

    def generateTotalExperience(self, player: Player):
        experience = player.get_experience()
        player.set_total_experience(player.get_total_experience() + experience)
  
    def generateTotalRoundWin(self, player: Player):
        roundWin = player.get_round_win()
        player.set_total_round_win(player.get_total_round_win() + roundWin)
        

    def round(self, firstTeam, secondTeam):
        [self.generateLuck(player) for player in firstTeam]
        [self.generateLuck(player) for player in secondTeam]

        [self.generateTotalExperience(player) for player in firstTeam]
        [self.generateTotalExperience(player) for player in secondTeam]

        scoreLaunchFirstTeam = [self.discountEndurance(player) for player in firstTeam]
        end = [self.calculateEnduranceRound(player) for player in firstTeam]

        
        self.firstTeamFinalScore += sum(scoreLaunchFirstTeam)
        scoreLaunchRoundFirstTeam = sum(scoreLaunchFirstTeam)

        scoreLaunchSecondTeam = [self.discountEndurance(player) for player in secondTeam]
        end1 = [self.calculateEnduranceRound(player) for player in secondTeam]

        
        self.secondTeamFinalScore += sum(scoreLaunchSecondTeam)
        scoreLaunchRoundSecondTeam = sum(scoreLaunchSecondTeam)
        self.raffleLaunch(firstTeam, secondTeam)

        self.findGroupRoundWinner(scoreLaunchRoundFirstTeam,scoreLaunchRoundSecondTeam, firstTeam, secondTeam)
        self.findIndividualRoundWinner(firstTeam, secondTeam)

        return scoreLaunchRoundFirstTeam, scoreLaunchRoundSecondTeam
    
    def finalGame(self, firstTeam:Team, secondTeam:Team):
        for player in firstTeam.players:
            player.set_enduranceRound(player.get_endurance())
            player.set_roundWin(0)
            player.set_experience(10)
            player.set_points(0)
            player.set_roundDiscount(0)
            player.set_total_experience(0)
            player.set_total_round_win(0)

        for player in secondTeam.players:
            player.set_enduranceRound(player.get_endurance())
            player.set_roundWin(0)
            player.set_experience(10)
            player.set_points(0)
            player.set_roundDiscount(0)
            player.set_total_experience(0)
            player.set_total_round_win(0)

        self.firstTeamFinalScore = 0
        self.secondTeamFinalScore = 0

        firstTeam.set_team_points(self.firstTeamFinalScore)
        secondTeam.set_team_points(self.secondTeamFinalScore)
    
    def raffleLaunch(self, firstTeam, secondTeam):
        score = 0
        playerFirstTeam = max(firstTeam, key=lambda player: player.get_luck()) 
        playerSecondTeam = max(secondTeam, key=lambda player: player.get_luck()) 

        if playerFirstTeam.get_luck() > playerSecondTeam.get_luck():
            self.firstTeamFinalScore += self.launch(playerFirstTeam)
            playerID = playerFirstTeam.get_player_id()
            endurance = (playerFirstTeam.get_endurance()) - 5
            score = self.ifPlayerWinsThreeLaunch(playerFirstTeam, playerID)
            score += self.firstTeamFinalScore
            return playerFirstTeam.get_luck(), self.firstTeamFinalScore
        else:
            self.secondTeamFinalScore += self.launch(playerSecondTeam)
            playerID = playerSecondTeam.get_player_id()
            endurance = (playerSecondTeam.get_endurance()) - 5
            score = self.ifPlayerWinsThreeLaunch(playerSecondTeam, playerID)
            score += self.secondTeamFinalScore
            return playerSecondTeam.get_luck(), self.secondTeamFinalScore

    def ifPlayerWinsThreeLaunch(self, player, playerID):
        launchAmount = 0
        score = 0
        if playerID == player.get_player_id():
            launchAmount += 1
            if launchAmount == self.consecutiveLaunches:
                score = self.launch(player)
        else:
            playerID = player.get_player_id()
            launchAmount = 0
        return score
        
    def findIndividualRoundWinner(self, firstTeam, secondTeam):
        winner = None
        playerFirstTeam = max(firstTeam, key=lambda player: player.get_points()) 
        playerSecondTeam = max(secondTeam, key=lambda player: player.get_points()) 

        if playerFirstTeam.get_points() > playerSecondTeam.get_points():
            newExperience = playerFirstTeam.get_experience() + 3
            playerFirstTeam.set_experience(newExperience)
            self.calculateIndividualWinnerRound(playerFirstTeam)
            winner = playerFirstTeam
        else: 
            newExperience = playerSecondTeam.get_experience() + 3
            playerSecondTeam.set_experience(newExperience)
            self.calculateIndividualWinnerRound(playerSecondTeam)
            winner = playerSecondTeam
        
        if playerFirstTeam.get_points() == playerSecondTeam.get_points():
            winner = self.defineWinnerInCaseOfTie(playerFirstTeam, playerSecondTeam)
        
        return winner
    
    def defineWinnerInCaseOfTie(self, playerFirstTeam, playerSecondTeam):
        winner = None
        scoreFirstTeamPlayer = self.launch(playerFirstTeam)
        playerFirstTeam.set_points(scoreFirstTeamPlayer)

        scoreSecondTeamPlayer = self.launch(playerSecondTeam)
        playerSecondTeam.set_points(scoreSecondTeamPlayer)
        if scoreFirstTeamPlayer > scoreSecondTeamPlayer:
            newExperience = playerFirstTeam.get_experience() + 3
            playerFirstTeam.set_experience(newExperience)
            self.calculateIndividualWinnerRound(playerFirstTeam)
            winner = playerFirstTeam
        else: 
            newExperience = playerSecondTeam.get_experience() + 3
            playerSecondTeam.set_experience(newExperience)
            self.calculateIndividualWinnerRound(playerSecondTeam)
            winner = playerSecondTeam
        return winner
    
    def calculateIndividualWinnerRound(self, player):
        roundWin = player.get_round_win() + 1
        player.set_roundWin(roundWin)
        return roundWin

    def findGroupRoundWinner(self, scoreRoundFirstTeam, scoreRoundSecondTeam, firstTeam, secondTeam):
        nameTeam1 = firstTeam
        nameTeam2 = secondTeam
        teamRoundWinner = " "
        if scoreRoundFirstTeam > scoreRoundSecondTeam:
            teamRoundWinner = "Ganador equipo1",nameTeam1
        else:
            teamRoundWinner = "Ganador equipo2", nameTeam2
        if scoreRoundFirstTeam == scoreRoundSecondTeam:
            teamRoundWinner = "No hay un ganador en esta ronda"
        return teamRoundWinner
    
    def playRounds(self, firstTeam:Team, secondTeam:Team):
        for _ in range(10):
            puntaje_equipo1, puntaje_equipo2 = self.round(firstTeam.players, secondTeam.players)
            
            [self.generateTotalRoundWin(player) for player in firstTeam.players]
            [self.generateTotalRoundWin(player) for player in secondTeam.players]

            self.firstTeamFinalScore += puntaje_equipo1
            self.secondTeamFinalScore += puntaje_equipo2

            firstTeam.set_team_points(self.firstTeamFinalScore)
            secondTeam.set_team_points(self.secondTeamFinalScore)
        return self.firstTeamFinalScore, self.secondTeamFinalScore, self.playerMoreLuck(firstTeam.players), self.playerMoreLuck(secondTeam.players), self.playerMoreExperience(firstTeam.players, secondTeam.players), self.findWinnerTeam(firstTeam, secondTeam), self.findGenderMoreWinsGame(firstTeam, secondTeam)

    # Función para determinar al jugador con más suerte en un equipo
    def playerMoreLuck(self, team):
        moreLuckyPlayer: Player = max(team, key=lambda player: player.get_average_lucky())
        return moreLuckyPlayer

    # Función para determinar al jugador con más experiencia en un juego
    def playerMoreExperience(self, firstTeam, secondTeam):
        playerMoreExperience = None
        playerFirstTeam = max(firstTeam, key=lambda player: player.get_total_experience()) 
        playerSecondTeam = max(secondTeam, key=lambda player: player.get_total_experience()) 

        if playerFirstTeam.get_total_experience() > playerSecondTeam.get_total_experience():
            playerMoreExperience = playerFirstTeam
        else: 
            playerMoreExperience = playerSecondTeam
        return playerMoreExperience
    
    def findWinnerTeam(self, firstTeam:Team, secondTeam:Team):
        if firstTeam.get_team_points() > secondTeam.get_team_points():
            return firstTeam 
        else:
            return secondTeam

    def findGenderMoreWinsGame(self, firstTeam:Team, secondTeam:Team):
        genderMoreWinsGame = None
        playerFirstTeam = max(firstTeam.players, key=lambda player: player.get_total_round_win()) 
        playerSecondTeam = max(secondTeam.players, key=lambda player: player.get_total_round_win()) 

        if playerFirstTeam.get_total_round_win() > playerSecondTeam.get_total_round_win():
            genderMoreWinsGame = playerFirstTeam
        else: 
            genderMoreWinsGame = playerSecondTeam
        return genderMoreWinsGame 

    def findIndividualWinner(self, firstTeam, secondTeam):
        winner = None
        playerFirstTeam = max(firstTeam, key=lambda player: player.get_round_win()) 
        playerSecondTeam = max(secondTeam, key=lambda player: player.get_round_win()) 

        if playerFirstTeam.get_round_win() > playerSecondTeam.get_round_win():
            winner = playerFirstTeam
        else: 
            winner = playerSecondTeam
        return winner
    

    def simulacion(self, num_juegos, firstTeam: Team, secondTeam: Team):
        resultados = []

        for _ in range(num_juegos):
            resultados.append(self.simulacion_round(firstTeam, secondTeam))
        
        return resultados


    # Función para simular múltiples juegos
    def simulacion_round(self, firstTeam: Team, secondTeam: Team):
        self.finalGame(firstTeam, secondTeam)
        self.firstTeamFinalScore, self.secondTeamFinalScore, playerMoreLuckFirstTeam, playerMoreLuckSecondTeam, playerMoreExperience, winnerTeam, genderWinnerGame = self.playRounds(firstTeam, secondTeam)
            
        if playerMoreLuckFirstTeam.get_average_lucky() > playerMoreLuckSecondTeam.get_average_lucky():
            playerMoreLucky = playerMoreLuckFirstTeam
        else:
            playerMoreLucky = playerMoreLuckSecondTeam

        resultGame = ResultGame(
            firstTeam, 
            secondTeam, 
            winnerTeam, 
            playerMoreLucky,
            playerMoreExperience,
            genderWinnerGame,
            genderWinnerGame
        )
    
        print("\n----------------------------------------------------------------\n")
        print("------------------------- GAME RESULT -------------------------")
        print("\n----------------------------------------------------------------\n")

        print(resultGame.__str__())
        print("\n----------------------------------------------------------------\n")

        return resultGame