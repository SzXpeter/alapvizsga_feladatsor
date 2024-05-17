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
        self.nev = data[0]
        self.eladasok = data[1]
        self.szeria = data[2]
        self.platform = data[3]
        self.megjelenes = data[4]
        self.fejleszto = data[5]
        self.kiado = data[6]

        if self.szeria == '':
            self.szeria = "None"

games: list[Game] = []

file = open("python/bestsellers.csv", 'r', encoding="UTF-8")
file.readline()
for row in file:
    games.append(Game(row))
file.close()

print(f"2. feladat: A fájlban {len(games)} játék adata szerepel.")

print("\n3. feladat: játékok-fejlesztők")
for game in games:
    print(f"{game.nev} -> {game.fejleszto}")

kiado = input("\n4. feladat: Kiadó megadása: ")
file = open(f"{kiado}.txt", 'w', encoding="UTF-8")
for game in games:
    if game.kiado.lower() == kiado.lower():
        print(game.nev)
        file.write(f"{game.nev} - {game.megjelenes}\n")
file.close()