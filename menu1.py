import random
import os
import math
            
def leiras():
    #játékmenet emlékeztetés a játékos felé
    print("\nJátékmenet:")
    print("1. Írja be a sor majd az oszlop számát (kötőjellel elválasztva), pl.:2-3")
    print("2. Ha megszeretné jelölni az aknát akkor Írjon Z (mint zászló) betüt a sor és oszlop után, pl.:2-3-Z\n")
    
def clear():
    os.system("clear")
    
class cella(object):
    ertek=0
    kival= False
    akna=False
    zaszlo=False
    def __init__(self):
        self.kival= False
    
    def __str__(self):
        return str(cella.ertek)

    def ezakna(self):
        if cella.ertek==-1:
            return True
        else: return False
        
    def ezzaszlo(self):
        if cella.ertek==-2:
            return True
        else:return False
        
class palyaosztaly(object):
    def __init__(self,a_sor,a_oszlop,a_akna,FileNev):
        self.FileNev=FileNev
        self.palya=[[cella() for i in range(a_oszlop)] for j in range(a_sor)]
        self.sor=a_sor
        self.oszlop=a_oszlop
        self.akna=a_akna
        self.valaszthatocella=a_sor * a_oszlop - a_akna
        n=0
        self.zaszlosz=int(a_akna)
        #aknák random elhelyezése
        while n<self.akna:
            randsor=random.randint(0,self.sor-1)
            randoszlop=random.randint(0,self.oszlop-1)
            if not self.palya[randsor][randoszlop].akna:
                self.pluszakna(randsor,randoszlop)
                n+=1
            
    #pálya kirajzolás, felnyitott cellák megjelenitése
    def __str__(self):
        rt = "  "
        div = "\n___"

        for i in range(1, self.oszlop+1):
            if i<10:
                rt += "  |  " + str(i)
                div += "______"
            else:
                rt += "  | " + str(i)
                div += "_______"
        div += "\n"
        st_2=" "
        rt+= div
        for s in range(0, self.sor):
            if s<9:
                rt += st_2
                rt+=str(s+1)
            else:
                rt += str(s+1)
                
            for o in range(0, self.oszlop):
                if self.palya[s][o].akna and self.palya[s][o].kival:
                    if self.palya[s][o].ezzaszlo and self.palya[s][o].ertek==-2:
                        rt += "  | " + "Z"
                    else:
                        rt += "  | " + "A"
                elif self.palya[s][o].kival:
                    rt += "  |  " + str(self.palya[s][o].ertek)
                else:
                    rt += "  |   "
            if o<10:
                rt += " |"
            else:
                rt += "  |"
            rt += div
        return rt
    #akna értéke, akna körüli cellák feltöltése számokkal
    def pluszakna(self,s,o):
        self.palya[s][o].ertek=-1
        self.palya[s][o].akna=True
        for i in range(s-1, s+2):
            if i >= 0 and i < self.oszlop:
                if o-1 >= 0 and not self.palya[i][o-1].akna:
                    self.palya[i][o-1].ertek += 1
                if o+1 < self.oszlop and not self.palya[i][o+1].akna:
                    self.palya[i][o+1].ertek += 1
        if s-1 >= 0 and not self.palya[s-1][o].akna:
            self.palya[s-1][o].ertek += 1
        if s+1 < self.sor and not self.palya[s+1][o].akna:
            self.palya[s+1][o].ertek += 1
            
    #rekurzioval nézi a felnyitott cellák körülötti cellákat
    def lepes(self,s,o):
        self.palya[s][o].kival=True
        self.valaszthatocella -= 1
        if self.palya[s][o].ertek==-1:
            return False
        if self.palya[s][o].ertek==0:
            for i in range(s-1,s+2):
                if i>=0 and i<self.sor:
                    if o-1>=0 and not self.palya[i][o-1].kival:
                        self.lepes(i,o-1)
                    if o+1 < self.oszlop and not self.palya[i][o+1].kival:
                        self.lepes(i, o+1)
            if s-1 >= 0 and not self.palya[s-1][o].kival:
                self.lepes(s-1, o)
            if s+1 < self.sor and not self.palya[s+1][o].kival:
                self.lepes(s+1, o)
            return True
        else:
            return True
        
    #amennyiben az input aknára mutat
    def aknaralep(self,s,o):
        return self.palya[s][o].ertek==-1
    
    #ha vége a játéknak, győzelem ellenőrzés
    def nyert(self):
        if self.valaszthatocella==0 or self.zaszlosz==0 or (self.valaszthatocella)+(self.zaszlosz)==0:
            return True
    
    def ures(self,s,o):
        if self.palya[s][o].ertek==0:
            return True
        
    def zaszlo(self,s,o):
        #csak abban az esetben engedi a zászlózást ha az akna, ez részben rossz, hirtelen csak így tudtam megoldani
        
        self.palya[s][o].kival=True
        if self.palya[s][o].ertek==-1:
            self.palya[s][o].ertek=-2
            self.palya[s][o].zaszlo=True
            self.zaszlosz=-1
            return True
        else:
            return False
    #-------------MENTÉS HELYE--------------
    def mentes(self,FileNev,s,o):
        menteshelye='C:\\Users\\168846\\Documents\\akna\\palyak' #Átkell irni!
        mentes=os.path.join(menteshelye,self.FileNev+".txt")
        
        f=open(mentes, "wt",encoding="utf-8")
        for i in range(s):
            for j in range(o):
                f.write(f"{self.palya[i][j].ertek} ")
            print("*",end="")    
            f.write("\n")
        f.close()
    
def beolvas():
    #kivételkezelés, visszahívás, ha rossz szám
    van=False
    while van==False:
        try:
            be=input("Adja meg a pálya méreteit vesszővel elválasztva(sor,oszlop)(max:99,99): ")
            sor=int(be.split(",")[0])
            oszlop=int(be.split(",")[1])
            #ajánlott aknaszám ismertetése a játékossal ami a cellák 20%-a felfele kerekítve
            ajanlott=math.ceil(sor*oszlop*0.20)
            print(f"Az ajánlott aknaszám (20%) >={ajanlott}")
            akna=input("Adja meg az aknák számát: ")
            akna=int(akna)
            #Ha több az akna mint a cella, vagy ha 0 akna van, akkor visszahív
            if akna>=sor*oszlop or akna==0:
                print("\nAknák száma 0 vagy meghaladja a pálya celláinak a számát")
                print(f"pálya celláinak a száma: {oszlop*sor} aknák száma: {akna}")
                print("Próbáld meg ujra megadni az adatokat\n")
                van=False
            #Ha meghaladja a 99x99 es határokat akkor is visszahív
            elif sor<100 and oszlop<100:
                akna=int(akna)
                sor=int(sor)
                oszlop=int(oszlop)
                return sor, oszlop, akna
                van=True
            else:
                print("A határokat meghaladata, maradjon azokon belül(max:99,99)! ")
                van=False
        except ValueError:
            print("Rosszul adta meg a méreteket!")
            print("\nPróbáld meg ujra megadni az adatokat")
            van=False
            
def menu1():
    futas=True
    while futas:
        adatok=beolvas()
        ment=input("Adja meg a mentés nevét: ")
        zaszlok=[]
        vege=False
        nyert=False
        palya=palyaosztaly(adatok[0],adatok[1],adatok[2],ment)
        palya.mentes(ment,adatok[0],adatok[1])
        while not vege:
            leiras()
            print(palya)
            be=input("Adja meg a sort és az oszlopot(kötöjellel elválasztva): ").split("-")
            if len(be)==2:
                try:
                    #Ellenörzés a helyes bemenetre
                    belista=list(map(int,be))
                except ValueError:
                    clear()
                    print("Rosszul adta meg!")
                    leiras()
                    continue
                #Zászlók kezelése(Próbálkozás)
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
                if belista[0]>adatok[0] or belista[0]<1 or belista[1]>adatok[1] or belista[1]<1:
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
                    #Tényleges jelölés, ha van még zászlód
                if len(zaszlok)<adatok[2]:
                    clear()
                    print("A cellát megjelöltük a zászlóval")
                    zaszlok.append([s,o])
                    palya.zaszlo(s,o)
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
            if belista[0]>adatok[0] or belista[0]<1 or belista[1]>adatok[1] or belista[1]<1:
                clear()
                print("Rosszul adta meg!")
                leiras()                
            s=belista[0]-1
            o=belista[1]-1
            #Ha a cellán zászló van akkor kivesszük abból a listából
            if [s,o]in zaszlok:
                zaszlok.remove([s,o])
            else:
                palya.lepes(s,o)
                vege=palya.aknaralep(s,o)
                if palya.nyert() and vege==False:
                    vege=True
                    nyert=True
        print(palya)
        if nyert:
            print("Gratulálok, Nyert!")
            clear()
            vege=True
            futas=False
        else:
            print("Aknára lépett, veszített!")
            clear()
            vege=True
            futas=False

