import math
import random
import discord

client=discord.Client()

class Jugador:
    def __init__(self, letra):
        self.letra=letra
        
    def movimiento_obtener(self,game):
        pass

class jugador_bot(Jugador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def movimiento_obtener(self,game):
        cuadro=random.choice(game.available_moves())
        return cuadro

class jugador_humano(Jugador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def movimiento_obtener(self,game):
        valid_cuadro=False
        val=None
        while not valid_cuadro:
            cuadro=input(self.letra+"'s turn. Input move (0-8): ")
            
            try:
                val=int(cuadro)
                if val not in game.available_moves():
                    raise ValueError
                valid_cuadro=True
            except ValueError:
                print("Invalid cuadro. Try again")
        return val

class jugador_bot_dificil(Jugador):
    def __init__(self,letra):
        super().__init__(letra)
    
    def movimiento_obtener(self,game):
        if len(game.available_moves())==9:
            cuadro=random.coice(game.available_moves())
        else:
            cuadro=self.minimax(game,self.letra)["position"]
        return cuadro
    
    def minimax(self,state,Jugador):
        max_Jugador=self.letra
        other_Jugador="O" if Jugador =="X" else "X"
        
        if state.current_winner==other_Jugador:
            return {"position":None,
                    "score": 1*(state.num_empty_cuadros()+1) if other_Jugador == max_Jugador else -1*(
                    state.num_empty_cuadros()+1)
                    }
        elif not state.empty_cuadros():
            return {"position":None, "score":0}
        
        if Jugador== max_Jugador:
            best={"position":None,"score":-math.inf}
        else:
            best={"position":None,"score":math.inf}
        
        for possible_move in state.available_moves():
            state.make_move(possible_move,Jugador)
            
            sim_score=self.minimax(state,other_Jugador)
            
            state.board[possible_move]=" "
            state.current_winner=None
            sim_score["position"]=possible_move
            
            if Jugador==max_Jugador:
                if sim_score["score"]>best["score"]:
                    best=sim_score
            else:
                if sim_score["score"]<best["score"]:
                    best=sim_score
        
        return best
