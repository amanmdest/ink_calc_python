class Comodo:
    #opcional:
    __largura: float
    __profundidade: float
    __altura: float

    #método mágico "_init_":
    def __init__(self, largura, profundidade, altura): #_init_ e um método construtor dentro da classe
        self.largura = largura
        self.profundidade = profundidade
        self.altura = altura

    @property 
    #Decorator => indica que esse método é uma propriedade de um atributo/uma forma de controlar o acesso a atributos privados
    def largura(self):
        return self.__largura

    @property 
    def profundidade(self):
        return self.__profundidade

    @property 
    def altura(self):
        return self.__altura    

    @largura.setter
    def largura(self, largura):
        try:  
        #estrutura try except serve para tratar erros
            self.__largura = float(largura)
        except Exception: 
            #exception permitirá a captura de qualquer tipo de erro
            print('O valor informado da largura é inválido')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:  
            self.__profundidade = float(profundidade)
        except Exception:
                print('O valor informado da profundidade é inválido')
                exit()

    @altura.setter
    def altura(self, altura):
        try:
            self.__altura = float(altura)
        except Exception:
                print('O valor informado da altura é inválido')
                exit()

