import numpy as np

class RandomWalk():
    """
    Clase RandomWalk
    Input: 
        - dim: numero de dimensiones del randomwalk
    
    """
    def __init__(self, dimension, distancia = 1):
        self.dimension = dimension
        self.distancia = distancia
        self.posicion = np.zeros(shape=(self.dimension), dtype=int)
        self.posiciones = []
        self.posiciones.append(self.posicion.copy())

    def generadorAleatorio(self):
        """
        genera un numero aleatorio entre las opciones posibles
        las opciones son: dimension, pero puedo elegir ir hacia
        delante o atras para ello, elijo entre 2*dimensiones
        si la eleccion es menor que dimensiones entonces avanzo
        si le eleccion es mayor que dimensiones retrocedo
        """
        return np.random.randint(2 * self.dimension)
    
    def modificarDistancia(self):
        a = self.generadorAleatorio()
        if a < self.dimension:
            self.posicion[a] += self.distancia
        else:
            self.posicion[a - self.dimension] -= self.distancia
    
    def origen(self):
        return (self.posicion == np.zeros(shape=(self.dimension), dtype=int)).all()
    
    def caminar(self, iteraciones):
        for _ in range(iteraciones -1):
            self.modificarDistancia()
            self.posiciones.append(self.posicion.copy())
            if self.origen():
                break
        return self.posiciones
    
    def paso(self):
        self.modificarDistancia()
        self.posiciones.append(self.posicion.copy())
        
