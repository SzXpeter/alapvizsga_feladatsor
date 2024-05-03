"""
beolvasás
hány játék szerepel a tartományban
játékok kiírása
bekérdezés->kiadók játékai
"""

# Név;Eladások;Széria;Platform;Megjelenes;Fejlesztő;Kiadó
class Game:
    def __init__(self, row):
        data = row.strip().split(';')
        nev = data[1]
        eladasok = data[2]
        szeria = data[3]
        platform = data[4]
        megjelenes = data[5]
        fejleszto = data[6]
        kiado = data[7]

games: list[Game] = []

file = open("bestsellers.csv", 'r', encoding="UTF-8")
for row in file:
    games.append(Game(row))