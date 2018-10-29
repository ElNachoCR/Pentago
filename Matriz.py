## Esta Clase representa cada cuadrante de 3 x 3
## que tiene el tablero
class Matriz:
    def __init__(self, x, y):
        self.matriz = [[0,0,0],[0,0,0],[0,0,0]]
        self.x = x # Posicion inicial de la ficha superior izquierda 
        self.y = y # Posicion inicial de la ficha superior izquierda
    
    ## Este metodo se encarga de rotar una matriz hacia la izquierda
    ## una vez
    ## Entradas:
    ##      La matriz
    ## Salidas:
    ##      Matriz rotada a la izquierda
    ## Restricciones:
    ##      None
    def rotacionIzq(self):
        nuevaMatriz = []
        cont = 3
        while cont != 0:
            nuevaFila = []
            for f in range(len(self.matriz)):
                nuevaFila.append(self.matriz[f][cont-1])
            nuevaMatriz.append(nuevaFila)
            cont -= 1
        
        self.matriz = nuevaMatriz
            
    ## Este metodo se encarga de rotar una matriz hacia la derecha
    ## una vez
    ## Entradas:
    ##      La matriz
    ## Salidas:
    ##      Matriz rotada a la derecha
    ## Restricciones:
    ##      None    
    def rotacionDer(self):
        nuevaMatriz = []
        cont = 0
        while cont < len(self.matriz):
            nuevaFila = []
            for f in range(len(self.matriz)):
                nuevaFila.append(self.matriz[f][cont])
            nuevaMatriz.append(nuevaFila)
            cont += 1
            
        for fila in nuevaMatriz:
            valor0 = fila[0]
            valor2 = fila[2]
            fila[0] = valor2
            fila[2] = valor0 
            
        self.matriz = nuevaMatriz
                
    ## Este metodo representa cada cuadrante en el tablero
    ## con circulos de color cafe si nadie ha colocado una ficha,
    ## blanco si hay una ficha del jugador 1, o negro si hay una
    ## ficha del jugador 2.
    ## Entradas:
    ##      Matriz
    ## Salidas:
    ##      Matriz representada en el juego
    ## Restricciones:
    ##      None 
    def display(self):
        posX = self.x
        posY = self.y    
        for fila in self.matriz:
            posX = self.x
            for ficha in fila:
                if ficha == 0:
                    fill(75,10,0)
                elif ficha == 1:
                    fill(255)
                elif ficha == 2:
                    fill(00,0,0)
                
                ellipse(posX,posY,40,40)
                posX += 60
            posY += 70  
                
    
    