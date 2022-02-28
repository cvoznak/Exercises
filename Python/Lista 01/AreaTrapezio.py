#1. Faça um programa que calcule e mostre a área de um trapézio.
#Sabe-se que: A = ((base maior + base menor) * altura)

print("Cálculo da Área do trapézio:")
baseMaior = float(input("Dimensão da maior base: "))
baseMenor = float(input("Dimensão da menor base: "))
altura = float(input("Dimensão da altura: "))
area = (baseMaior + baseMenor) * altura

print(f"A área total do trazézio é {area:.2f}")