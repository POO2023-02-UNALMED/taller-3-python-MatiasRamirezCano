class TV:

    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        numTV +=1

    def setMarca(self, marca):
        self.marca = marca
    def getMarca(self):
        return self.marca
    def setCanal(self, canal):
        if (canal >= 1 and canal <= 120):
            self.canal = canal
    def getCanal(self):
        return self.canal
    def setPrecio(self, precio):
        self.precio = precio
    def getPrecio(self):
        return self.precio
    def setVolumen(self, volumen):
        self.volumen = volumen
    def getVolumen(self):
        return self.volumen
    def setControl(self, control):
        self.control = control
    def getControl(self):
        return self.control
    def getEstado(self):
        return self.estado
    
    @classmethod
    def setNumTV(self, numTV):
        self.numTV = numTV
    @classmethod    
    def getNumTV(self):
        return self.numTV
    
    def turnOn(self):
        if self.estado == False:
            self.estado = True
    def turnOff(self):
        if self.estado == True:
            self.estado = False
    
    def canalUp(self):
        if (self.estado == True and self.canal < 120):
            self.canal += 1   
    def canalDown(self):
        if (self.estado == True and self.canal > 1):
            self.canal -= 1
    def volumenUp(self):
        if (self.estado == True and self.volumen < 7):
            self.volumen += 1   
    def volumenDown(self):
        if (self.estado == True and self.volumen > 0):
            self.volumen -= 1