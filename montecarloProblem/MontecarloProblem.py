import tkinter as tk
from montecarloProblem.Game import Game
from tkinter import ttk
import matplotlib.pyplot as plt

from montecarloProblem.player import Player

class MontecarloProblem:
     
    cantidad_juegos = 0

    resultsGame = [] 

    def __init__(self, master):
        self.master = master
        self.master.title("MontecarloProblem")

        # Dimensiones de la ventana principal
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        ventana_width = int(screen_width * 0.5)
        ventana_height = int(screen_height * 0.5)

        # Coordenadas para centrar la ventana principal
        x = (screen_width - ventana_width) // 2
        y = (screen_height - ventana_height) // 2

        # Establecer el tamaño y posición de la ventana principal
        self.master.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

        # Etiqueta de título
        self.etiqueta = tk.Label(master, text="MontecarloProblem")
        self.etiqueta.pack()

        # Entrada para ingresar la cantidad de juegos
        self.cantidad_juegos_label = tk.Label(master, text="Ingrese la cantidad de juegos:")
        self.cantidad_juegos_label.pack()

        self.cantidad_juegos_entry = tk.Entry(master)
        self.cantidad_juegos_entry.pack()

        # Botón "Jugar"
        self.jugar_button = tk.Button(master, text="Jugar", command=self.abrir_opciones)
        self.jugar_button.pack()

    def abrir_opciones(self):
        self.cantidad_juegos = int(self.cantidad_juegos_entry.get())
        print(f"Jugando {self.cantidad_juegos} juegos...")
        
        self.resultsGame = self.start_game()

        # Crear una nueva ventana para mostrar las opciones
        self.opciones_window = tk.Toplevel(self.master)
        self.opciones_window.title("Opciones")

        # Dimensiones de la ventana emergente
        ventana_width = int(self.master.winfo_width() * 0.8)
        ventana_height = int(self.master.winfo_height() * 0.8)

        # Coordenadas para centrar la ventana emergente
        x = (self.master.winfo_screenwidth() - ventana_width) // 2
        y = (self.master.winfo_screenheight() - ventana_height) // 2

        # Establecer el tamaño y posición de la ventana emergente
        self.opciones_window.geometry(f"{ventana_width}x{ventana_height}+{x}+{y}")

        # Botones para cada opción
        self.jugador_suerte_button = tk.Button(self.opciones_window, text="Ver Jugador con más suerte en cada juego", command=self.mostrar_tabla_jugador_suerte)
        self.jugador_suerte_button.pack()

        self.jugador_experiencia_button = tk.Button(self.opciones_window, text="Ver Jugador que haya ganado más experiencia al final de cada juego", command=self.show_more_experience_player_table)
        self.jugador_experiencia_button.pack()

        self.equipo_ganador_button = tk.Button(self.opciones_window, text="Ver Equipo ganador incluyendo sus puntajes", command=self.show_winner_team)
        self.equipo_ganador_button.pack()

        self.genero_victorias_button = tk.Button(self.opciones_window, text="Ver Género con más victorias en cada juego", command=self.show_gender_more_winner_each_game_table)
        self.genero_victorias_button.pack()

        """self.genero_victorias_button = tk.Button(self.opciones_window, text="Ver Género con más victorias en total", command=self.show_gender_more_winner_total_table)
        self.genero_victorias_button.pack()"""

        self.grafica_puntos_button = tk.Button(self.opciones_window, text="Ver gráfica de los puntos obtenidos", command=self.show_scores_table)
        self.grafica_puntos_button.pack()

        # Botón "Volver"
        self.volver_button = tk.Button(self.opciones_window, text="Volver", command=self.opciones_window.destroy)
        self.volver_button.pack()

    def start_game(self):
        print("--------------------------------------------\nResultados") 
        game = Game()
        # Crear equipos
        firstTeam = game.create_teams("Equipo1")
        print(firstTeam.__str__())
        secondTeam = game.create_teams("Equipo2")
        print(secondTeam.__str__())
        resultados = game.simulacion(self.cantidad_juegos, firstTeam, secondTeam)
        return resultados

    def mostrar_tabla_jugador_suerte(self):
        data = []
        j = 1
        for i in self.resultsGame:
            currentLuckyPlayer:Player = i.get_more_lucky_player()
            data.append((j, 
                currentLuckyPlayer.get_player_id(), 
                currentLuckyPlayer.get_gender(), 
                currentLuckyPlayer.get_endurance(), 
                currentLuckyPlayer.get_total_experience(), 
                currentLuckyPlayer.get_average_lucky(),
                currentLuckyPlayer.get_points(),
                currentLuckyPlayer.get_total_round_win()))
            j = j + 1

        # Crear una nueva ventana para la tabla
        table = self.getTableSetUp("Jugador con más suerte")
        
        # Insertar los datos en la tabla
        for row in data:
            table.insert("", "end", values=row)

        # Empacar la tabla
        table.pack()

    def show_more_experience_player_table(self):
        data = []
        j = 1
        
        
        for i in self.resultsGame:
            currentExperiencePlayer = i.get_more_experience_player()
            data.append((j, 
                currentExperiencePlayer.get_player_id(), 
                currentExperiencePlayer.get_gender(), 
                currentExperiencePlayer.get_endurance(), 
                currentExperiencePlayer.get_total_experience(), 
                currentExperiencePlayer.get_average_lucky(), 
                currentExperiencePlayer.get_points(),
                currentExperiencePlayer.get_total_round_win()))
            j = j + 1

        # Crear una nueva ventana para la tabla
        table = self.getTableSetUp("Jugador con más experiencia")

        # Insertar los datos en la tabla
        for row in data:
            table.insert("", "end", values=row)

        # Empacar la tabla
        table.pack()

    def show_gender_more_winner_each_game_table(self):
        data = []
        j = 1

        for i in self.resultsGame:
            currentMoreWinnerEachGamePlayer = i.get_gender_more_winner_each_game()
            data.append((j, 
                currentMoreWinnerEachGamePlayer.get_player_id(), 
                currentMoreWinnerEachGamePlayer.get_gender(), 
                currentMoreWinnerEachGamePlayer.get_endurance(), 
                currentMoreWinnerEachGamePlayer.get_total_experience(), 
                currentMoreWinnerEachGamePlayer.get_average_lucky(), 
                currentMoreWinnerEachGamePlayer.get_points(),
                currentMoreWinnerEachGamePlayer.get_total_round_win()
                ))
            j = j + 1

        # Crear una nueva ventana para la tabla
        table = self.getTableSetUp("Genero con más victorias por cada juego")

        # Insertar los datos en la tabla
        for row in data:
            table.insert("", "end", values=row)

        # Empacar la tabla
        table.pack()
    
    def show_gender_more_winner_total_table(self):
        data = []
        j = 1
        
        for i in self.genderMoreWinnerTotal:
            data.append((j, i.get_gender(), i.get_endurance(), i.get_experience(), i.get_luck(), i.get_points()))
            j = j + 1

        # Crear una nueva ventana para la tabla
        table = self.getTableSetUp("Genero con más victorias en total")

        # Insertar los datos en la tabla
        for row in data:
            table.insert("", "end", values=row)

        # Empacar la tabla
        table.pack()

    def show_winner_team(self):
        data = []
        j = 0
        for i in self.resultsGame:
            currentWinnerTeam = i.get_winner_team()
            data.append((j, 
                currentWinnerTeam.get_team_name(), 
                currentWinnerTeam.get_team_points(),
                currentWinnerTeam.get_players()
                
                ))
            j = j + 1
        # Crear una nueva ventana para la tabla
        tabla_window = tk.Toplevel(self.opciones_window)
        tabla_window.title("Equipo ganador")

        # Crear un Treeview para mostrar la tabla
        tabla = ttk.Treeview(tabla_window, columns=("Juego", "Nombre Equipo", "Puntaje", "Jugadores"), show="headings")

        # Encabezados de las columnas
        tabla.heading("Juego", text="Juego")
        tabla.heading("Nombre Equipo", text="Nombre Equipo")
        tabla.heading("Puntaje", text="Puntaje")
        tabla.heading("Jugadores", text="Jugadores")        

        # Insertar los datos en la tabla
        for row in data:
            tabla.insert("", "end", values=row)

        # Empacar la tabla
        tabla.pack()
    #def show_table_results(self):


    def getTableSetUp(self, title:str):
        # Crear una nueva ventana para la tabla
        tabla_window = tk.Toplevel(self.opciones_window)
        tabla_window.title(title)

        # Crear un Treeview para mostrar la tabla
        tabla = ttk.Treeview(tabla_window, columns=("Juego", "ID", "Género", "Resistencia", "Experiencia", "Suerte", "Puntos", "Rondas ganadas"), show="headings")

        # Encabezados de las columnas
        tabla.heading("Juego", text="Juego")
        tabla.heading("ID", text="ID")
        tabla.heading("Género", text="Género")
        tabla.heading("Resistencia", text="Resistencia")
        tabla.heading("Experiencia", text="Experiencia")
        tabla.heading("Suerte", text="Suerte")
        tabla.heading("Puntos", text="Puntos")
        tabla.heading("Rondas ganadas", text="Rondas ganadas")

        return tabla
    
    def show_scores_table(self):
        dataFirst = []
        j = 0
        for i in self.resultsGame:
            currentFirstTeam = i.get_first_team()
            dataFirst.append((j, 
                currentFirstTeam.get_team_name(), 
                currentFirstTeam.get_team_points(),
                ))
            j = j + 1

        datasecond = []
        j = 0
        for i in self.resultsGame:
            currentSecondTeam = i.get_second_team()
            datasecond.append((j, 
                currentSecondTeam.get_team_name(), 
                currentSecondTeam.get_team_points(),
                ))
            j = j + 1

        # Extraer los nombres de los equipos y los puntajes
        teams_first = [entry[1] for entry in dataFirst]
        scores_first = [entry[2] for entry in dataFirst]

        teams_second = [entry[1] for entry in datasecond]
        scores_second = [entry[2] for entry in datasecond]

        # Graficar
        plt.scatter(teams_first, scores_first, color='blue', label='First Team')
        plt.scatter(teams_second, scores_second, color='green', label='Second Team')
        plt.xlabel('Team')
        plt.ylabel('Score')
        plt.title('Team Scores')
        plt.legend()
        plt.show()
