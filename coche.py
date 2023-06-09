class Coche:
    pass
    def __init__(self, marca: str, modelo: str, matricula:str) -> None:
        self.marca = marca
        self.modelo =modelo
        self.matricula = matricula
    def __str__(self) -> str:
        return f"{self.marca}- {self.modelo} - {self.matricula}"

    # def marca(self):
        
        

    
    # def modelo(self):

    # def matricula(self):

