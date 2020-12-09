import numpy as np
from numpy.lib.function_base import gradient

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
        

if __name__ == "__main__":
    import matplotlib.animation as animation
    import matplotlib.pyplot as plt
#    from IPython.display import HTML

    # plt.rcParams['figure.figsize'] = (5,5)
    # plt.rcParams['figure.dpi'] = 100
    # plt.rcParams['savefig.dpi'] = 100
    # plt.rcParams["animation.html"] = "jshtml"  # for matplotlib 2.1 and above, uses JavaScript

    rw1 = RandomWalk(3)  # 1 dimension
    rw2 = RandomWalk(3)
    rw3 = RandomWalk(3)

    def animate_func(i):
        global rw1, rw2, rw3
        global graph
        for i, rw in enumerate([rw1, rw2, rw3]):
            rw.paso()
            x[i].append(rw.posicion[0].copy())
            y[i].append(rw1.posicion[1].copy())
            z[i].append(rw1.posicion[2].copy())
            graph[i]._offsets3d = (x[i], y[i], z[i])
        return graph,


    x = [[0], [0], [0]]
    y = [[0], [0], [0]]
    z = [[0], [0], [0]]

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")
    graph = [None, None, None]
    graph[0] = ax.scatter(x[0], y[0], z[0], color='orange', marker = ".")
    graph[1] = ax.scatter(x[1], y[1], z[1], color='red', marker = ".")
    graph[2] = ax.scatter(x[2], y[2], z[2], color='green', marker = ".")


    ax.set_xlim3d(-20, 20)
    ax.set_ylim3d(-20, 20)
    ax.set_zlim3d(-20, 20)

    # # Creating the Animation object
    ani = animation.FuncAnimation(fig, animate_func, interval=1000, frames= 500, blit=False)
    plt.show()