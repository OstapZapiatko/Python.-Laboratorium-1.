#Zadanie 3 (3.py):• Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
#• Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
#• Dla osób powyżej 18 roku życia bilet kosztuje 20zł.
#Przykład: Wprowadź wiek klienta: 5
#Cena biletu: 10zł

x = int(input('napisz swój wiek: '))
if x <= 3:
    print('Wstęp jest bezpłatny')
elif 4 <= x <= 17:
    print('Bilet kosztuje 10zł')
elif x >= 18:
    print('Bilet kosztuje 20zł')

