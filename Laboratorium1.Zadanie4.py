#Zadanie 4 (4.py) Napisz skrypt, który sprawdzi czy litera wprowadzona przez użytkownika jest duża czy mała.

x = str(input("enter letter: "))
if str.isupper(x):
    print("Duża")
if str.islower(x):
    print("Mała")