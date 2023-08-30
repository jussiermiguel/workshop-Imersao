from abc import ABC, abstractmethod

class IAnimal(ABC):
    
    @abstractmethod
    def falar(self):
        """Defina na classe filha"""
    
    @abstractmethod
    def andar(self):
        """Defina na classe filha"""
        
        
class Cachorro(IAnimal):
    """def falar(self):
        return super().falar()"""
    def falar(self):
        print("AuAu")
        
    def andar(self):
        print("Ando com 4 patas")
        
class Pessoa:
    
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self.idade = idade
        self.__humano = True
    
    def fala_pessoa(self):
        print("Falando")
        
    def mostra_nome(self):
        print(self._nome)
        
    def mostra_idade(self):
        print(self.idade)
        
#animal = IAnimal()
pingo = Cachorro()
pingo.falar()
pingo.andar()

humano = Pessoa("Jussier", 21)
humano.fala_pessoa()
humano.mostra_nome()
humano.mostra_idade()