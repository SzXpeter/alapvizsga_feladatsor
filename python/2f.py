"""
Találd ki a számot játék.
Generál a gép egy számot 1 és 10 között
a játékosnak 3 tippje van
a program megmondja, hogy a szám kisebb, v nagyobb a tippnél
a végénél megkérdezi, hogy szeretne-e újra játszani
"""
import random

def main():
    while True:
        if tipp_mix() < 3:
            print("Gratulálok nyert.")
        else:
            print("Sajnálom vesztett.")

        vege = ""
        while vege != "I" and vege !="N":
            vege = input("Szeretne még egyet játszani: Igen(I)/Nem(N) ")
        if vege == "N":
            break

def bekeres():
    while True:
        try:
            tipp = int(input("Adjon meg egy tippet: "))
        except:
            pass
        else:
            return tipp

def tipp_mix():
    szam = random.randint(1, 10)
    print(f"{szam = }")
    i = 0
    while i < 3:
        tipp = bekeres()
        if szam > tipp:
            print(f"A szám nagyobb mint {tipp}.")
        elif szam < tipp:
            print(f"A szám kisebb mint {tipp}.")
        else:
            break
        i += 1
    return i

main()