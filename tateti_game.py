from tateti_player import jugador_humano,jugador_bot#,jugador_bot_dificil
import time
import discord

client=discord.Client()

class tateti:
    def __init__(self):
        self.tablero=[" " for _ in range(9)]
        self.jugador_ganador=None
    
    def tablero_mostrar(self):
        for fila in [self.tablero[i*3:(i+1)*3] for i in range(3)]:
            print ("| " + " | ".join(fila)+" |")
    
    @staticmethod
    def tablero_mostrar_nums():
        tablero_numero=[[str(i) for i in range(j*3,(j+1)*3)] for j in range (3)]
        for fila in tablero_numero:
            print("| " + " | ".join(fila)+" |")
    
    def movimientos_disponibles(self):
        return [i for i, spot in enumerate(self.tablero) if spot==" "]

    def lugares_vacios(self):
        return " " in self.tablero

    def num_lugares_vacios(self):
        return self.tablero.count(" ")
    
    def movimientos_realizar(self,cuadro,letra):
        if self.tablero[cuadro]==" ":
            self.tablero[cuadro]=letra
            if self.ganador(cuadro,letra):
                self.jugador_ganador=letra
            return True
        return False
    
    def ganador(self,cuadro,letra):
        fila_indice=cuadro//3
        fila=self.tablero[fila_indice*3:(fila_indice+1)*3]
        if all([spot==letra for spot in fila]):
            return True
        
        col_indice=cuadro%3
        columna=[self.tablero[col_indice+i*3] for i in range(3)]
        if all([spot==letra for spot in columna]):
            return True
        
        if cuadro%2==0:
            diagonal1=[self.tablero[i] for i in [0,4,8]]
            if all([spot==letra for spot in diagonal1]):
                return True
            diagonal2=[self.tablero[i] for i in [2,4,6]]
            if all([spot==letra for spot in diagonal2]):
                return True
        
        return False
    
def play(game, x_player, o_player, game_mostrar=True):
    if game_mostrar:
        game.tablero_mostrar_nums()
    
    letra = "X"
    while game.lugares_vacios():
        if letra=="O":
            cuadro=o_player.get_move(game)
        else:
            cuadro=x_player.get_move(game)
        
        if game.movimientos_realizar(cuadro,letra):
            if game_mostrar:
                game.tablero_mostrar()
                print(letra+ f" pone su pieza en {cuadro}")
                print("")
            
            if game.jugador_ganador:
                if game_mostrar:
                    print("¡El jugador "+letra + " gana!")
                return letra
            
            letra="O" if letra =="X" else "X"
        
        if game_mostrar:
           time.sleep(0.8)
    
    if game_mostrar:
        print("¡Es un empate!")

@client.event
async def tateti_launch(mensaje):
    if mensaje.author == client.user:
        return

    await mensaje.channel.send("¡TaTeTi!")
    await mensaje.channel.send("¿Desea jugar contra el bot o contra otro jugador?")
    choice=input("").upper()
    if choice =="Y":
        #HAY QUE PONER PARA JUGAR CONTRA EL BOT
        x_player=jugador_humano("X")
        o_player=jugador_bot("O")
        t=tateti()
        play(t,x_player,o_player,game_mostrar=True)
        #Y OPCION DE JUGAR CONTRA EL SUPER BOT O BOT RANDOM
    elif choice == "N":
        pass #Y JUGAR CONTRA EL BOT
    else: 
        await mensaje.channel.send("Wrong input. Please try again")
