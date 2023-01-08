#Zadanie 5 (5.py) Napisz program działający jak prosty kalkulator, który potrafi dodawać, odejmować,
#mnożyć, dzielić oraz obliczać potęgę.Przykład: Jaką operację chcesz wykonać?
#1) dodawanie
#2) odejmowanie
#3) mnożenie
#4) dzielenie
#5) potęgowanie
#Wpisz numer operacji: 2
#Podaj argument 1: 34
#Podaj argument 2: 5
#Wynik: 29


x = (int(input('Wpisz numer operacji:')))
a = (int(input('Podaj argument 1: ')))
b = (int(input('Podaj argument 2: ')))
if x == 1:
    print(float(a + b))
elif x == 2:
    print(float(a - b))
elif x == 3:
    print(float(a * b))
elif x == 4:
    print(float(a / b))
elif x == 5:
    print(float(a ** b))
else: print('Prosze wybrać operacje ot 1 do 5')



