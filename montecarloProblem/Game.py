import random
from montecarloProblem.Team import Team
from montecarloProblem.player import Player
class Game:
    
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
            if player.gender == 'mujer':
                precision = [0.3, 0.68, 0.95, 1.0]  # Probabilidades acumuladas para las categorías de precisión
                puntajes = [10, 9, 8, 0]            # Puntajes correspondientes a cada categoría de precisión
            else:
                precision = [0.2, 0.55, 0.95, 1.0]   # Probabilidades acumuladas para las categorías de precisión
                puntajes = [10, 9, 8, 0]            # Puntajes correspondientes a cada categoría de precisión

            # Generamos un número aleatorio entre 0 y 1 para determinar la categoría de precisión
            random_number = random.random()
            for i in range(len(precision)):
                if random_number <= precision[i]:
                    puntaje = puntajes[i]
                    break
            return puntaje
    
    def discountEndurance(self,player):
        points = 0
        endurance = player.get_endurance()
        while endurance >= 5:
            points += self.launch(player)
            endurance -= 5
            break
        return points

    def calculateEnduranceRound(self, player):
        endurance = player.get_endurance()
        enduranceRound = endurance - int(random.randint(1, 2))
        player.set_enduranceRound(enduranceRound)
        #print(player)
        return enduranceRound
    
    def generateLuck(self, player):
        #luck = player.get_luck()
        player.set_luck(luck)

    def ronda(self, equipo1, equipo2):
        lanzamientos_equipo1 = [self.discountEndurance(jugador) for jugador in equipo1]
        end = [self.calculateEnduranceRound(jugador) for jugador in equipo1]
        print(lanzamientos_equipo1)
        for jug in equipo1:
            print(jug)
        puntaje_equipo1 = sum(lanzamientos_equipo1)

        lanzamientos_equipo2 = [self.discountEndurance(jugador) for jugador in equipo2]
        end1 = [self.calculateEnduranceRound(jugador) for jugador in equipo2]
        print(lanzamientos_equipo2)
        for jug1 in equipo2:
            print(jug1)
        puntaje_equipo2 = sum(lanzamientos_equipo2)
        return puntaje_equipo1, puntaje_equipo2
    
    def finalGame(self, equipo1, equipo2):
        for player in equipo1:
            player.set_enduranceRound(player.get_endurance())
            print(player)
        for player in equipo2:
            player.set_enduranceRound(player.get_endurance())
            print(player)


