import math
import random


class Jugador:
    def __init__(self, letra):
        self.letra=letra
        
    def movimiento_obtener(self,juego):
        pass

class jugador_bot(Jugador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def movimiento_obtener(self,juego):
        cuadro=random.choice(juego.movimientos_disponibles())
        return cuadro

class jugador_humano(Jugador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def movimiento_obtener(self,juego):
        cuadro_valido=False
        val=None
        while not cuadro_valido:
            cuadro=input("Es el turno de "+self.letra+". Ingrese una posición válida (0-8): ")
            
            try:
                val=int(cuadro)
                if val not in juego.movimientos_disponibles():
                    raise ValueError
                cuadro_valido=True
            except ValueError:
                print("Posición inválida. Intente de nuevo")
        return val

class jugador_bot_dificil(Jugador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def movimiento_obtener(self,juego):
        if len(juego.movimientos_disponibles())==9:
            cuadro=random.choice(juego.movimientos_disponibles())
        else:
            cuadro=self.minimax(juego,self.letra)["posicion"]
        return cuadro
    
    def minimax(self,state,Jugador):
        max_Jugador=self.letra
        otro_Jugador="O" if Jugador =="X" else "X"
        
        if state.jugador_ganador==otro_Jugador:
            return {"posicion":None,
                    "score": 1*(state.num_lugares_vacios()+1) if otro_Jugador == max_Jugador else -1*(
                    state.num_lugares_vacios()+1)
                    }
        elif not state.lugares_vacios():
            return {"posicion":None, "score":0}
        
        if Jugador== max_Jugador:
            optimo={"posicion":None,"score":-math.inf}
        else:
            optimo={"posicion":None,"score":math.inf}
        
        for movimiento_posible in state.movimientos_disponibles():
            state.movimientos_realizar(movimiento_posible,Jugador)
            
            sim_score=self.minimax(state,otro_Jugador)
            
            state.tablero[movimiento_posible]=" "
            state.jugador_ganador=None
            sim_score["posicion"]=movimiento_posible
            
            if Jugador==max_Jugador:
                if sim_score["score"]>optimo["score"]:
                    optimo=sim_score
            else:
                if sim_score["score"]<optimo["score"]:
                    optimo=sim_score
        
        return optimo
