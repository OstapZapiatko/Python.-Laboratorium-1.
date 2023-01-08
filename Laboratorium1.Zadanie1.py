#print('''Napisz skrypt, który pobiera długości boków prostokąta, a następnie oblicza jego pole i obwód
#oraz wyświetla wyniki na ekranie.''')

print("Napisz długość boku a")
a = int(input())
print("Napisz długość boku b")
b = int(input())


S = a * b
P = (a+b) * 2

print("Pole prostokąta", S)
print("Obwód prostokąta", P)