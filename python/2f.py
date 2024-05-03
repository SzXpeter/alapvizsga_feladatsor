"""
Találd ki a számot játék.
Generál a gép egy számot 1 és 10 között
a játékosnak 3 tippje van
a program megmondja, hogy a szám kisebb, v nagyobb a tippnél
a végénél megkérdezi, hogy szeretne-e újra játszani
"""
import random

def bekeres():
    tipp = 0
    while True:
        try:
            tipp = int(input("Adjon meg egy tippet: "))
        except:
            pass
        else:
            return tipp

def main():
    while True:
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
        
        if i < 3:
            print("Gratulálok nyert.")
        else:
            print("Sajnálom vesztett.")

        vege = ""
        while vege != "I" and vege !="N":
            vege = input("Szeretne mégegyet játszan: Igen(I)/Nem(N)")
        if vege == "N":
            break


main()