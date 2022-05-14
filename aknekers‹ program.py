#Menü fv.
import sys
import os
import menu1
import menu2

def clear():
    os.system("clear")
def menu():
    print("Menü",
        "1. Új játék létrehozása és a pálya mentése",
        "2. Egy már létrehozott pálya újrajátszása",
        "9. Kilepes",
          sep="\n")
    try:
        parancs=int(input())
        if parancs==1:

            return 1
        elif parancs==2:
            return 2
        elif parancs==9:
            return 9
            clear()
        else:
            clear()
            print("Rossz számot adtál meg, próbáld újra!")
                
    except ValueError:
        clear()
        print("Nem számot adtál meg, próbáld újra")
            

def main():
    prog=True
    while prog:
        szam=int(menu())
        if szam==1:
            print("\nÚj játék létrehozása és mentése\n")
            menu1.menu1()
        elif szam==2:
            print("\nEgy már létrehozott pálya újrajátszása\n")
            menu2.menu2()
        else:
            print("KILÉPETT A JÁTÉKBÓL")
            sys.exit()
            
main()
