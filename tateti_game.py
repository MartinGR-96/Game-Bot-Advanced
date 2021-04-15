from tateti_player import jugador_humano, jugador_bot, jugador_bot_dificil
import time
import discord

client=discord.Client()

class tateti:
    def __init__(self):
        self.tablero = [" " for _ in range(9)]
        self.jugador_ganador = None

    def tablero_mostrar(self):
        for fila in [self.tablero[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(fila) + " |")

    @staticmethod
    def tablero_mostrar_nums():
        tablero_numero = [[str(i) for i in range(j * 3, (j + 1) * 3)]
                          for j in range(3)]
        for fila in tablero_numero:
            print("| " + " | ".join(fila) + " |")

    def movimientos_disponibles(self):
        return [i for i, posicion in enumerate(self.tablero) if posicion == " "]

    def lugares_vacios(self):
        return " " in self.tablero

    def num_lugares_vacios(self):
        return self.tablero.count(" ")

    def movimientos_realizar(self, cuadro, letra):
        if self.tablero[cuadro] == " ":
            self.tablero[cuadro] = letra
            if self.ganador(cuadro, letra):
                self.jugador_ganador = letra
            return True
        return False

    def ganador(self, cuadro, letra):
        fila_indice = cuadro // 3
        fila = self.tablero[fila_indice * 3:(fila_indice + 1) * 3]
        if all([posicion == letra for posicion in fila]):
            return True

        col_indice = cuadro % 3
        columna = [self.tablero[col_indice + i * 3] for i in range(3)]
        if all([posicion == letra for posicion in columna]):
            return True

        if cuadro % 2 == 0:
            diagonal1 = [self.tablero[i] for i in [0, 4, 8]]
            if all([posicion == letra for posicion in diagonal1]):
                return True
            diagonal2 = [self.tablero[i] for i in [2, 4, 6]]
            if all([posicion == letra for posicion in diagonal2]):
                return True

        return False


def jugar(juego, jugador_x, jugador_o, juego_mostrar=True):
    if juego_mostrar:
        juego.tablero_mostrar_nums()

    letra = "X"
    while juego.lugares_vacios():
        if letra == "O":
            cuadro = jugador_o.movimiento_obtener(juego)
        else:
            cuadro = jugador_x.movimiento_obtener(juego)

        if juego.movimientos_realizar(cuadro, letra):
            if juego_mostrar:
                juego.tablero_mostrar()
                print(letra + f" pone su pieza en {cuadro}")
                print("")

            if juego.jugador_ganador:
                if juego_mostrar:
                    print("¡El jugador " + letra + " gana!")
                return letra

            letra = "O" if letra == "X" else "X"

        if juego_mostrar:
            time.sleep(0.8)

    if juego_mostrar:
        print("¡Es un empate!")

@client.event
async def tateti_launch(mensaje):
  if mensaje.author == client.user:
    return

  await mensaje.channel.send("¡TaTeTi!")
  await mensaje.channel.send("¿Desea jugar contra otro jugador o contra el bot?")
  
  if mensaje.content.startswith("!1"):
      jugador_x = jugador_humano("X")
      jugador_o = jugador_humano("O")
      t = tateti()
      jugar(t, jugador_x, jugador_o, juego_mostrar=True)
  elif mensaje.content.startswith("!2"):
      mensaje.channel.send("¿Contra el bot fácil o el bot invencible?")
      if mensaje.content.startswith("!1"):
        jugador_x = jugador_humano("X")
        jugador_o = jugador_bot("O")
        t = tateti()
        jugar(t, jugador_x, jugador_o, juego_mostrar=True)
      elif mensaje.content.startswith("!2"):
        jugador_x = jugador_humano("X")
        jugador_o = jugador_bot_dificil("O")
        t = tateti()
        jugar(t, jugador_x, jugador_o, juego_mostrar=True)
  else:
      await mensaje.channel.send("Opción invalida, intente de nuevo.")
