class Televisao:
    def __init__(self, marca):
        self.marca = marca
        self.volume = 0
    
    #MÉTODOS   
    def aumentar_volume(self):
        if self.volume < 10:
            self.volume = self.volume + 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume = self.volume - 1
            
    def visualizar_atributos(self):
        print("TV Marca:", self.marca)
        print("---Volume:", self.volume)
            
def ler_marca_tv():
    return input("Insira o nome da marca da sua TV: ")

tv_sala = Televisao(ler_marca_tv())
tv_dormitorio = Televisao(ler_marca_tv())

tv_sala.visualizar_atributos()

tv_dormitorio.aumentar_volume()
tv_dormitorio.aumentar_volume()
tv_dormitorio.aumentar_volume()
tv_dormitorio.diminuir_volume()

tv_dormitorio.visualizar_atributos()
