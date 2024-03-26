import random
from montecarloProblem.Team import Team
from montecarloProblem.player import Player
import matplotlib.pyplot as plt
import pandas as pd
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
            #Team.add_player(player)
        team = Team(name=name, players=players)
        #print(team)
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
    
    def discountEndurance(self,player):
        points = 0
        endurance = player.get_endurance()
        while endurance >= 5:
            points += self.launch(player)
            endurance -= 5
            player.set_points(points)
        return points

    def calculateEnduranceRound(self, player):
        endurance = player.get_endurance_round()
        enduranceRound = 0
        #print(player)
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

    def generateLuck(self, player):
        player.set_luck(random.uniform(1, 3))

    def round(self, firstTeam, secondTeam):
        [self.generateLuck(player) for player in firstTeam]
        [self.generateLuck(player) for player in secondTeam]

        scoreLaunchFirstTeam = [self.discountEndurance(player) for player in firstTeam]
        end = [self.calculateEnduranceRound(player) for player in firstTeam]
        print(scoreLaunchFirstTeam)

        
        self.firstTeamFinalScore += sum(scoreLaunchFirstTeam)
        scoreLaunchRoundFirstTeam = sum(scoreLaunchFirstTeam)

        scoreLaunchSecondTeam = [self.discountEndurance(player) for player in secondTeam]
        end1 = [self.calculateEnduranceRound(player) for player in secondTeam]
        print(scoreLaunchSecondTeam)

        
        self.secondTeamFinalScore += sum(scoreLaunchSecondTeam)
        scoreLaunchRoundSecondTeam = sum(scoreLaunchSecondTeam)
        self.raffleLaunch(firstTeam, secondTeam)

        self.findGroupRoundWinner(scoreLaunchRoundFirstTeam,scoreLaunchRoundSecondTeam, firstTeam, secondTeam)
        self.findIndividualRoundWinner(firstTeam, secondTeam)

        for jug in firstTeam:
            print(jug)
        print("\n")
        for jug1 in secondTeam:
            print(jug1)

        print(self.firstTeamFinalScore)
        print(self.secondTeamFinalScore)
        return scoreLaunchRoundFirstTeam, scoreLaunchRoundSecondTeam
    
    def finalGame(self, firstTeam:Team, secondTeam:Team):
        for player in firstTeam.players:
            player.set_enduranceRound(player.get_endurance())
            player.set_roundWin(0)
            player.set_experience(10)
            player.set_points(0)
            player.set_roundDiscount(0)
            print(player)
        for player in secondTeam.players:
            player.set_enduranceRound(player.get_endurance())
            player.set_roundWin(0)
            player.set_experience(10)
            player.set_points(0)
            player.set_roundDiscount(0)
            print(player)
        self.firstTeamFinalScore = 0
        self.secondTeamFinalScore = 0
    
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
            print("El puntaje con el sorteo ganado:",score)
            return playerFirstTeam.get_luck(), self.firstTeamFinalScore
        else:
            self.secondTeamFinalScore += self.launch(playerSecondTeam)
            playerID = playerSecondTeam.get_player_id()
            endurance = (playerSecondTeam.get_endurance()) - 5
            score = self.ifPlayerWinsThreeLaunch(playerSecondTeam, playerID)
            score += self.secondTeamFinalScore
            print("El puntaje con el sorteo ganado:", score)
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
#tal vez aquí se necesite  --> 
        playerFirstTeam.set_points(scoreFirstTeamPlayer)

        scoreSecondTeamPlayer = self.launch(playerSecondTeam)
#igual acá
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
        #print(teamRoundWinner)
        return teamRoundWinner
    
    def playRounds(self, firstTeam:Team, secondTeam:Team):
        for _ in range(10):
            puntaje_equipo1, puntaje_equipo2 = self.round(firstTeam.players, secondTeam.players)
            self.firstTeamFinalScore += puntaje_equipo1
            self.secondTeamFinalScore += puntaje_equipo2
        #self.finalGame(firstTeam.players, secondTeam.players)
        return self.firstTeamFinalScore, self.secondTeamFinalScore, self.playerMoreLuck(firstTeam.players), self.playerMoreLuck(secondTeam.players), self.playerMoreExperience(firstTeam.players, secondTeam.players), self.findWinnerTeam(firstTeam, secondTeam), self.findGenderMoreWinsGame(firstTeam, secondTeam)

    # Función para determinar al jugador con más suerte en un equipo
    def playerMoreLuck(self, team):
        return max(team, key=lambda player: player.get_luck())

    # Función para determinar al jugador con más experiencia en un juego
    def playerMoreExperience(self, firstTeam, secondTeam):
        playerMoreExperience = None
        playerFirstTeam = max(firstTeam, key=lambda player: player.get_experience()) 
        playerSecondTeam = max(secondTeam, key=lambda player: player.get_experience()) 

        if playerFirstTeam.get_experience() > playerSecondTeam.get_experience():
            playerMoreExperience = playerFirstTeam
        else: 
            playerMoreExperience = playerSecondTeam
        return playerMoreExperience
    
    def findWinnerTeam(self, firstTeam:Team, secondTeam:Team):
        #self.playRounds(firstTeam, secondTeam)
        print("\n")
        print(self.firstTeamFinalScore)
        print(self.secondTeamFinalScore)
        if self.firstTeamFinalScore > self.secondTeamFinalScore:
            return firstTeam 
        else:
            return secondTeam

    def findGenderMoreWinsGame(self, firstTeam:Team, secondTeam:Team):
        genderMoreWinsGame = None
        playerFirstTeam = max(firstTeam.players, key=lambda player: player.get_round_win()) 
        playerSecondTeam = max(secondTeam.players, key=lambda player: player.get_round_win()) 

        if playerFirstTeam.get_round_win() > playerSecondTeam.get_round_win():
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
        #print(winner.get_round_win())
        return winner
    
    # Función para simular múltiples juegos
    def simulacion(self, num_juegos, firstTeam: Team, secondTeam: Team):
        resultados = {
            'jugador_mas_suerte': [],
            'jugador_mas_experiencia': [],
            'equipo_ganador': [],
            'genero_victorias en cada juego': [],
            'genero_victorias totales': [],
            'puntajes_juego': []
        }
        for _ in range(num_juegos):
            # Reset game data
            self.finalGame(firstTeam, secondTeam)

            self.firstTeamFinalScore, self.secondTeamFinalScore, playerMoreLuckFirstTeam, playerMoreLuckSecondTeam, playerMoreExperience, winnerTeam, genderWinnerGame = self.playRounds(firstTeam, secondTeam)
            resultados['puntajes_juego'].append((self.firstTeamFinalScore, self.secondTeamFinalScore))
            resultados['jugador_mas_suerte'].append(playerMoreLuckFirstTeam if playerMoreLuckFirstTeam.get_luck() > playerMoreLuckSecondTeam.get_luck() else playerMoreLuckSecondTeam)
            resultados['jugador_mas_experiencia'].append(playerMoreExperience)
            resultados['equipo_ganador'].append(winnerTeam)
            resultados['genero_victorias en cada juego'].append(genderWinnerGame)
            genderTotal = self.findGenderMoreWinsGame(firstTeam, secondTeam)
            resultados['genero_victorias totales'].append(genderTotal)    

            print("final", self.firstTeamFinalScore)
            print("final", self.secondTeamFinalScore)
        return resultados
    
        # Función para generar tablas
    def mostrar_resultados(self, resultados):
        print("Resultados de la simulación:")
        print("----------------------------")

        # Tabla de jugador con más suerte
        print("Jugador con más suerte:")
        df_luck = pd.DataFrame([(i+1, jugador.get_gender(), jugador.get_endurance(), jugador.get_experience(), jugador.get_luck()) for i, jugador in enumerate(resultados['jugador_mas_suerte'])], columns=['Juego', 'Género', 'Resistencia', 'Experiencia', 'Suerte'])
        print(df_luck)
        print()

        # Tabla de jugador con más experiencia
        print("Jugador con más experiencia:")
        df_experience = pd.DataFrame([(i+1, jugador.get_gender(), jugador.get_endurance(), jugador.get_experience(), jugador.get_luck()) for i, jugador in enumerate(resultados['jugador_mas_experiencia'])], columns=['Juego', 'Género', 'Resistencia', 'Experiencia', 'Suerte'])
        print(df_experience)
        print()

        # Tabla de equipo ganador
        print("Equipo ganador:")
        df_winner = pd.DataFrame([(i+1, ganador, resultados['puntajes_juego'][i][0], resultados['puntajes_juego'][i][1]) for i, ganador in enumerate(resultados['equipo_ganador'])], columns=['Juego', 'Ganador', 'Puntaje Equipo 1', 'Puntaje Equipo 2'])
        print(df_winner)
        print()

        # Género con más victorias en cada juego
        print("Género con más victorias en cada juego:")
        df_gender_per_game = pd.DataFrame([(i+1, jugador.get_gender(), jugador.get_endurance(), jugador.get_experience(), jugador.get_luck(), jugador.get_round_win()) for i, jugador in enumerate(resultados['genero_victorias en cada juego'])], columns=['Juego', 'Género', 'Resistencia', 'Experiencia', 'Suerte', 'victoria'])
        print(df_gender_per_game)
        print()

        # Género con más victorias totales
        print("Género con más victorias totales:")
        df_gender_total = pd.DataFrame([(i+1, jugador.get_gender(), jugador.get_endurance(), jugador.get_experience(), jugador.get_luck(), jugador.get_round_win()) for i, jugador in enumerate(resultados['genero_victorias totales'])], columns=['Juego', 'Género', 'Resistencia', 'Experiencia', 'Suerte', 'victoria'])
        print(df_gender_total)
        print()
   
    def graficar_puntajes(self,resultados):
        puntajes_equipo1 = [x[0] for x in resultados['puntajes_juego']]
        puntajes_equipo2 = [x[1] for x in resultados['puntajes_juego']]
        juegos = range(1, len(puntajes_equipo1) + 1)

        plt.plot(juegos, puntajes_equipo1, label='Equipo 1', marker='o')
        plt.plot(juegos, puntajes_equipo2, label='Equipo 2', marker='o')
        plt.xlabel('Juego')
        plt.ylabel('Puntaje')
        plt.title('Puntajes por Juego')
        plt.legend()
        plt.grid(True)
        plt.show()
    

