from calculadora import Calculator
from comodo import Comodo

calc = Calculator()

comodo = Comodo(
    input("Digite a largura do cômodo: "),
    input("Digite a altura do cômodo: "),
    input("Digite a profundidade do cômodo: "))

print("A área das paredes é:", calc.calcular_area_paredes(comodo))
print("A área do teto é:", calc.calcular_area_teto(comodo))
print("A litragem de tinta necessária é:", calc.calcular_litragem_necessaria())