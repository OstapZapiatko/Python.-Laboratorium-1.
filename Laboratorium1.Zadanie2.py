#print('''Zadanie 2 (2.py) Napisz skrypt, który pobiera od użytkownika drogę pokonaną przez samochód oraz średnie
#spalanie (w litrach na 100 km) i wyświetli informację o przewidywanym zużyciu paliwa oraz o szacowanych
#kosztach podróży (cena paliwa 6.5 zł/l)''')

x = int(input('drogę pokonaną przez samochód(km): '))
y = int(input('średnie spalanie (w litrach na 100 km): '))

#f = informację o przewidywanym zużyciu paliwa
#k = szacowani koszty podróży

f = x * y/100
k = f * 6.5
z = 'zł'
l = 'l'
print('przewidywane zużyciu paliwa' , f , l)
print('szacowani koszty podróży' , k , z)