import os
import glob
def leiras():
    #játékmenet emlékeztetés a játékos felé
    print("\nJátékmenet:")
    print("1. Írja be a sor majd az oszlop számát (kötőjellel elválasztva), pl.:2-3")
    print("2. Ha megszeretné jelölni az aknát akkor Írjon Z (mint zászló) betüt a sor és oszlop után, pl.:2-3-Z")
    
def clear():
    os.system("clear")
    #-------------BEOLVASÁS HELYE--------------
def fajlok():
    fileok=[]
    os.chdir("C:\\Users\\168846\\Documents\\akna\\palyak") #Átkell irni!
    for file in glob.glob("*.txt"):
        print(file)
        fileok.append(file)
    return fileok
        
def beolvas(Filenev):
    hivas='C:\\Users\\168846\\Documents\\akna\\palyak' #Átkell irni!
    teljes=os.path.join(hivas,Filenev)
    f=open(teljes,"rt",encoding="utf-8")
    ertekek=[]
    for sor in f:
        szamstring = sor.split()
        szamok = [int(n) for n in szamstring] 
        ertekek.append(szamok)
    sor=int(len(ertekek))
    oszlop=int(len(ertekek[0]))
    aknasz=0
    for i in range(sor):
        for j in range(oszlop):
            if ertekek[i][j]==-1:
                aknasz+=1
    return ertekek,sor,oszlop,aknasz

def palya(ertekek,sor,oszlop):
    global jlista
    print("\t\tAKNAKERESŐ\n")
    st = "   "
    #oszlop számozás
    for i in range(oszlop):
        if i<10:
            st = st + "     " + str(i + 1)
        #ha kétjegyű számok vannak akkor egy space-el kevesebb
        else:
            st = st + "    " + str(i + 1)
    print(st)   
 
    for s in range(sor):
        st = "     "
        if s == 0:
            for o in range(oszlop):
                st = st + "______" 
            print(st)
 
        st = "     "
        for o in range(oszlop):
            st = st + "|     "
        print(st + "|")
        #sor számozás
        #ha kétjegyű számok vannak akkor egy space-el kevesebb
        if s>8:
            st = " " + str(s + 1) + "  "
        else:
            st = "  " + str(s + 1) + "  "
        for o in range(oszlop):
            #a megjeleníthető cellák kiírása
            st = st + "|  " + str(jlista[s][o]) + "  "
        print(st + "|") 
 
        st = "     "
        for o in range(oszlop):
            st = st + "|_____"
        print(st + '|')
 
    print()
    
#rekurzív hívás, ami nézi a szomszédos elemeket, és ugy bontja ki a "0"-as cellákat
def szomszedos(ertekek,sor,oszlop,s,o):
    global jlista
    global latogatott
    #Ha még nem néztük a cellát
    if [s,o] not in latogatott:
        latogatott.append([s,o])
        #ha 0 cella
        if ertekek[s][o]==0:
            #háttér listábol átemelem a megjelenítendőbe
            jlista[s][o]=ertekek[s][o]

            #rekurziv visszahívások
            if o<oszlop-1:
                szomszedos(ertekek,sor,oszlop,s,o+1)
            if o>0:
                szomszedos(ertekek,sor,oszlop,s,o-1)
            if s<sor-1:
                szomszedos(ertekek,sor,oszlop,s+1,o)
            if s>0:
                szomszedos(ertekek,sor,oszlop,s-1,o)
            if s>0 and o>0:
                szomszedos(ertekek,sor,oszlop,s-1,o-1)
            if s>0 and o<oszlop-1:
                szomszedos(ertekek,sor,oszlop,s-1,o+1)
            if s>sor-1 and o>0:
                szomszedos(ertekek,sor,oszlop,s+1,o-1)
            if s>sor-1 and o<oszlop-1:
                szomszedos(ertekek,sor,oszlop,s+1,o+1)
        #Ha nem "0" érték, akkor csak azt a cellát viszem át
        if ertekek[s][o]!=0:
            jlista[s][o]=ertekek[s][o]
            
def aknamutatas(ertekek,sor,oszlop):
    global jlista
    for s in range(sor):
        for o in range(oszlop):
            if ertekek[s][o]==-1:
                jlista[s][o]='A'
                
def jatekvege(sor,oszlop,akna):
    global jlista
    n=0
    for s in range(sor):
        for o in range(oszlop):
            if jlista[s][o]!=' ' and jlista !='Z':
                #megszámolja azokat a cellákat, amik megvannak jelenítve, és nincsen rajtuk zászló 
                n+=1
    if n==sor*oszlop-akna:
        return True
    else: return False
    
def menu2():
    global jlista
    global latogatott
    print("Kérem válasszon az alábbi pályák közül és írja be a nevét")
    fajlok()
    rossz=True
    while rossz:
        fajln=input("\nA választott pálya: ")
        if fajln in fajlok():
            rossz=False   
        else:
            rossz
            print("\nRosszul adta meg, kérem próbálja újra!")
        
    zaszlok=[]
    vege=False
    ertekek=beolvas(fajln)[0]
    sor=int(beolvas(fajln)[1])
    oszlop=int(beolvas(fajln)[2])
    akna=int(beolvas(fajln)[3])
    jlista = [[' ' for i in range(oszlop)] for j in range(sor)]
    while not vege:
        leiras()
        palya(ertekek,sor,oszlop)
        be=input("Adja meg a sort és az oszlopot(kötöjellel elválasztva): ").split("-")
            #Sima cella nézés
        if len(be)==2:
            try:
                #Ellenörzés a helyes bemenetre
                belista=list(map(int,be))
            except ValueError:
                clear()
                print("Rosszul adta meg!")
                leiras()
                continue
        #Zászlók kezelése
        elif len(be)==3:
            if be[2]!='z' and be[2]!='Z':
                clear()
                print("Rosszul adta meg!")
                leiras()
                continue
            try:
                #Ellenörzés a helyes bemenetre
                belista=list(map(int,be[:2]))
            except ValueError:
                clear()
                print("Rosszul adta meg!")
                leiras()
                continue
            #Ellenörzés, hogy a megadott cella benne van-e a pályában
            if belista[0]>beolvas(fajln)[1] or belista[0]<1 or belista[1]>beolvas(fajln)[2] or belista[1]<1:
                clear()
                print("Rosszul adta meg!")
                leiras()
                continue
            s=belista[0]-1
            o=belista[1]-1
            #Ha már van ott zászló
            if [s,o] in zaszlok:
                clear()
                print("A cellát már megjelölted")
                continue
            #Ha már egy érték van ott
            if jlista[s][o]!=' ':
                clear()
                print("A cella értékét már tudjuk")
                continue
            #Tényleges jelölés, ha van még zászlód
            if len(zaszlok)<beolvas(fajln)[3]:
                clear()
                print("A cellát megjelöltük a zászlóval")
                zaszlok.append([s,o])
                jlista[s][o]='Z'
                continue
            else:
                clear()
                print("Zászlózást befejeztük")
                continue
        else:
            clear()
            print("Rosszul adta meg!")
            leiras()
            continue
            
        #Ellenörzés, hogy a megadott cella benne van-e a pályában
        if belista[0]>beolvas(fajln)[1] or belista[0]<1 or belista[1]>beolvas(fajln)[2] or belista[1]<1:
            clear()
            print("Rosszul adta meg!")
            leiras()
            continue
        
        s=belista[0]-1
        o=belista[1]-1
        #Ha a cellán zászló van akkor kivesszük abból a listából
        if [s,o]in zaszlok:
            zaszlok.remove([s,o])
                
        #Ha aknára lépett a játékos
        if (beolvas(fajln)[0])[s][o]==-1:
            jlista[s][o]=='A'
            #Összes akna kiírása
            aknamutatas(beolvas(fajln)[0],beolvas(fajln)[1],beolvas(fajln)[2])
            #Pálya megmutatása
            palya(beolvas(fajln)[0],beolvas(fajln)[1],beolvas(fajln)[2])
            print("Aknára lépett, játéknak vége!")
            vege=True
            continue
        #Ha "0"-as cellára lépett, hívjuk a rekurziv fv.-t
        elif (beolvas(fajln)[0])[s][o]==0:
            latogatott=[]
            jlista[s][o]='0'
            szomszedos(beolvas(fajln)[0],beolvas(fajln)[1],beolvas(fajln)[2],s,o)

        #Ha egy szimpla értékre lépett,(1-8)
        else:
            jlista[s][o]=(beolvas(fajln)[0])[s][o]
            
        #Ellenörzés
        if(jatekvege(beolvas(fajln)[1],beolvas(fajln)[2],beolvas(fajln)[3])):
            #Feltérképezett pálya megmutatása
            aknamutatas(beolvas(fajln)[0],beolvas(fajln)[1],beolvas(fajln)[2])
            palya(beolvas(fajln)[0],beolvas(fajln)[1],beolvas(fajln)[2])
            print("Gratulálok, megnyerte a játékot!")
            vege=True
            continue
        clear()

