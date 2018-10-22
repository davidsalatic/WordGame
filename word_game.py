from tkinter import *
import random
import threading
import time
from tkinter import messagebox

class Game:

    def __init__(self):
        self.lines_1=[line.rstrip('\n') for line in open('Recnici\\recnik_1.txt')] #smestanje txt fajla sa recima od 1 slova
        self.lines_2 = [line.rstrip('\n') for line in open('Recnici\\recnik_2.txt')] #smestanje txt fajla sa recima od 2 slova
        self.lines_3 = [line.rstrip('\n') for line in open('Recnici\\recnik_3.txt')] #...
        self.lines_4 = [line.rstrip('\n') for line in open('Recnici\\recnik_4.txt')]
        self.lines_5 = [line.rstrip('\n') for line in open('Recnici\\recnik_5.txt')]
        self.lines_6 = [line.rstrip('\n') for line in open('Recnici\\recnik_6.txt')]
        self.lines_7 = [line.rstrip('\n') for line in open('Recnici\\recnik_7.txt')]
        self.lines_8 = [line.rstrip('\n') for line in open('Recnici\\recnik_8.txt')]
        self.lines_9 = [line.rstrip('\n') for line in open('Recnici\\recnik_9.txt')]
        self.lines_10 = [line.rstrip('\n') for line in open('Recnici\\recnik_10.txt')]
        self.lines_11 = [line.rstrip('\n') for line in open('Recnici\\recnik_11.txt')]
        self.lines_12 = [line.rstrip('\n') for line in open('Recnici\\recnik_12.txt')]
        self.lblWord = Label(root, text="", bg="Wheat2", width=60, height=5, fg="RoyalBlue3", font="Helvetica 12 bold") #ovde radi lakseg azuriranja teksta na ekranu
        self.word="" #rec koju je igrac napravio
        self.btn1_isactive=1 #belezim koji dugmici su mi aktivni, 1=aktivan,0=neaktivan, jer iako se dugme disabluje kad se klikne na njega i dalje aktivira event, tako da samo vizuelno deaktivira dugme
        self.btn2_isactive=1
        self.btn3_isactive=1
        self.btn4_isactive=1
        self.btn5_isactive=1
        self.btn6_isactive=1
        self.btn7_isactive=1
        self.btn8_isactive=1
        self.btn9_isactive=1
        self.btn10_isactive=1
        self.btn11_isactive=1
        self.btn12_isactive=1
        self.lblMinimumLetters = Label(root, text=str(player.level)+". nivo: minimum reč od " + str(player.level + 2) + " slova",
                                  font="Helvetica 14 italic", bg="wheat3",
                                  fg="gray16")  # igrac mora da napravi rec najmanje 2 slova vecu od trenutnog levela zato je min=level+2, kao atribut klase je zbog lakseg pristupanja preko self.
        self.lblBalance = Label(root, text=str(player.cash)+"$", bg="Wheat3", fg="sea green", font="Helvetica 20 bold") #dole levo prikazuje $, ovde radi lakseg azuriranja

    def checkDictionary(self,event):
        iterator = 0 #iterator za petlju
        found = 0 #indikator da li rec koju je igrac napravio postoji u recniku (0=false 1=true)
        validLength = 0 #indikator da li rec koju je igrac napravio odgovara zahtevu za minimalnu duzinu (0=false 1=true)

        if (len(self.word) == 1): #ako je korisnik napravio rec od 1 karaktera,ta rec se pretrazuje u txt fajlu sa svim recima sa duzinom karaktera 1
            while (iterator != len(self.lines_1)):  # ide od 0 do kolko ima reci u tekstualnom fajlu
                if self.lines_1[iterator].lower() == self.word:  # ako je rec koju je korisnik napravio postoji u recniku. lower() koristim jer u fajlu postoje reci sa velikim pocetnim slovom
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 2): #ako je korisnik napravio rec od 2 karaktera,ta rec se pretrazuje u txt fajlu sa svim recima sa duzinom karaktera 2
            while (iterator != len(self.lines_2)):  # ide od 0 do kolko ima reci u tekstualnom fajlu
                if self.lines_2[iterator].lower() == self.word:  # ako je rec koju je korisnik napravio postoji u recniku
                    found = 1 #tada stavljamo da je nadjena rec u recniku
                    if len(self.word) >= (player.level + 2): #ako rec odgovara zahtevu za minimalnu duzinu reci
                        validLength = 1  #tada stavljamo da je minimalna duzina reci zadovoljena
                iterator += 1
        elif (len(self.word) == 3):
            while (iterator != len(self.lines_3)):  # -||-
                if self.lines_3[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 4):
            while (iterator != len(self.lines_4)):
                if self.lines_4[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 5):
            while (iterator != len(self.lines_5)):
                if self.lines_5[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 6):
            while (iterator != len(self.lines_6)):
                if self.lines_6[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 7):
            while (iterator != len(self.lines_7)):
                if self.lines_7[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 8):
            while (iterator != len(self.lines_8)):
                if self.lines_8[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 9):
            while (iterator != len(self.lines_9)):
                if self.lines_9[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 10):
            while (iterator != len(self.lines_10)):
                if self.lines_10[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 11):
            while (iterator != len(self.lines_11)):
                if self.lines_11[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        elif (len(self.word) == 12):
            while (iterator != len(self.lines_12)):
                if self.lines_12[iterator].lower() == self.word:
                    found = 1
                    if len(self.word) >= (player.level + 2):
                        validLength = 1
                iterator += 1
        if (found == 0 and validLength==0):
            self.lblWord.config(fg="red") #ako rec nije pronadjena u recniku tada rec postane crvene boje
        elif (found ==1 and validLength==0):
            self.lblWord.config(fg="orange") #ako rec postoji u recniku, ali nije dovoljno dugacka da zadovolji zahtev postane narandzasta
        elif (found==1 and validLength==1):
            self.lblWord.config(fg="green") #ako rec postoji u recniku i dovoljno je dugacka, slova postanu zelena
        else:
            print("Error coloring words!")

    def clearWord(self,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12):
        self.lblWord.config(text="") #brisanje teksta iz polja sa napisanom reci
        self.word="" #resetoavnje promenljive (rec koju igrac pravi)
        self.btn1_isactive = 1 #ispod je aktiviranje svih dugmica
        btn1.config(state="normal")
        self.btn2_isactive = 1
        btn2.config(state="normal")
        self.btn3_isactive = 1
        btn3.config(state="normal")
        self.btn4_isactive = 1
        btn4.config(state="normal")
        self.btn5_isactive = 1
        btn5.config(state="normal")
        self.btn6_isactive = 1
        btn6.config(state="normal")
        self.btn7_isactive = 1
        btn7.config(state="normal")
        self.btn8_isactive = 1
        btn8.config(state="normal")
        self.btn9_isactive = 1
        btn9.config(state="normal")
        self.btn10_isactive = 1
        btn10.config(state="normal")
        self.btn11_isactive = 1
        btn11.config(state="normal")
        self.btn12_isactive = 1
        btn12.config(state="normal")

    def submitWord(self,event):
        iterator = 0
        found = 0
        validLength=0
        if player.runThread!=0: #ako je program u aktivnoj fazi,tj thread za odbrojavanje sekundi traje, kod u ovom if-u se nece desiti ako program ceka da korisnik zapocne novi nivo,jer tad je runthread=0
            if (len(self.word) == 1):
                while (iterator != len(self.lines_1)): #istin nacin pretrage recnika kao u metodi clearWord()
                    if self.lines_1[iterator].lower() == self.word: #lower() jer su neke reci u txt fajlu sa pocetnim velikim slovom
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 2):
                while (iterator != len(self.lines_2)):
                    if self.lines_2[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 3):
                while (iterator != len(self.lines_3)):
                    if self.lines_3[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 4):
                while (iterator != len(self.lines_4)):
                    if self.lines_4[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 5):
                while (iterator != len(self.lines_5)):
                    if self.lines_5[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 6):
                while (iterator != len(self.lines_6)):
                    if self.lines_6[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 7):
                while (iterator != len(self.lines_7)):
                    if self.lines_7[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 8):
                while (iterator != len(self.lines_8)):
                    if self.lines_8[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 9):
                while (iterator != len(self.lines_9)):
                    if self.lines_9[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 10):
                while (iterator != len(self.lines_10)):
                    if self.lines_10[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 11):
                while (iterator != len(self.lines_11)):
                    if self.lines_11[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1
            elif (len(self.word) == 12):
                while (iterator != len(self.lines_12)):
                    if self.lines_12[iterator].lower() == self.word:
                        found = 1
                        if len(self.word)>=(player.level+2):
                            validLength=1
                    iterator += 1

            if (found == 0 and validLength==0): #ako rec ne postoji u recniku
                messagebox.showerror("Ups!", "Data rec ne postoji u recniku!")
                self.lblWord.config(fg="red")
            elif (found ==1 and validLength==0): #ako rec postoji u recniku al nije dovoljno dugacka
                messagebox.showwarning("Za mrvicu!","Rec koju si uneo nije dovoljno dugacka! Rec mora da sadrzi najmanje "+str(player.level+2)+" slova!")
                self.lblWord.config(fg="orange")
            elif (found==1 and validLength==1): #ako rec zadovoljava uslov i postoji u recniku
                if player.level!=6: #kada nije poslednji nivo
                    self.lblWord.config(text='Cestitamo. Za rec "'+self.word+'" osvojio si '+str(len(self.word))+" $! Za sledeci nivo klikni na ✔",fg="green") #tekst koji se ispisuje
                    player.cash+=len(self.word) #dodaje se cash-a koliko je dugacka rec
                    self.lblBalance.config(text=str(player.cash)+"$", bg="Wheat3", fg="sea green", font="Helvetica 20 bold") #updatuje se label u kom pise cash balance
                    player.runThread=0 #zaustavlja se thread kako ne bi odbrojavao sekunde
                    player.level+=1 #dodajemo level
                    player.seconds=60 #resetuje se broj sekundi na 60
                    self.btn1_isactive=0 #disablujemo sve dugmice da dok ne pokrene sledeci nivo ne moze da unosi slova
                    self.btn2_isactive=0
                    self.btn3_isactive=0
                    self.btn4_isactive=0
                    self.btn5_isactive=0
                    self.btn6_isactive=0
                    self.btn7_isactive=0
                    self.btn8_isactive=0
                    self.btn9_isactive=0
                    self.btn10_isactive=0
                    self.btn11_isactive=0
                    self.btn12_isactive=0
                else: #if player.level==6kad je poslednji nivo i uspesno je nasao rec
                    player.runThread=0
                    self.lblWord.config(text="CESTITAMO! CESTITAMO! CESTITAMO!",fg="purple")
                    yes_no = messagebox.askquestion("Cestitamo!","Presao si sve nivoe! Zelis li da pocnes ispocetka?")
                    if yes_no == 'yes': #ako je izabrao da igra opet...
                        player.list_of_sets = [player.set_0, player.set_1, player.set_2, player.set_3, #popunjavaju se opet sve kombinacije jer su neke obrisane koje su bile
                                               player.set_4,player.set_5, player.set_6, player.set_7, player.set_8,
                                               player.set_9, player.set_10, player.set_11, player.set_12, player.set_13,
                                               player.set_14, player.set_15, player.set_16, player.set_17,
                                               player.set_18, player.set_19]
                        player.level=1 #vracanje na prvi level kako bi igra krenula ispocetka
                        self.lblMinimumLetters.config(
                            text=str(player.level) + ". nivo: minimum reč od " + str(player.level + 2) + " slova",
                            font="Helvetica 14 italic", bg="wheat3",
                            fg="gray16") #podesavanje teksta na kom pise kolko je najmanje slova potrebno
                        self.btn1_isactive = 1  # aktiviranje svih dugmica
                        self.btn2_isactive = 1
                        self.btn3_isactive = 1
                        self.btn4_isactive = 1
                        self.btn5_isactive = 1
                        self.btn6_isactive = 1
                        self.btn7_isactive = 1
                        self.btn8_isactive = 1
                        self.btn9_isactive = 1
                        self.btn10_isactive = 1
                        self.btn11_isactive = 1
                        self.btn12_isactive = 1
                        player.cash=0 #vracanje $ na 0
                        self.lblBalance.config(text=str(player.cash)+"$", bg="Wheat3", fg="sea green", font="Helvetica 20 bold") #vracanje label za cash$ na 0
                        player.seconds = 60

                        self.generateLetters()  # pravim novi set slova, u toj metodi se takodje resetuje rec koju igrac pravi na prazno
                    else: #ako nece da zapocne novu igru...
                        root.destroy()#program se gasi

            else:
                print("Error")

        else: #----SLEDECI NIVO -----
            #else uslov- desi se samo ako je thread stopiran tj player.runThread==0, do kog dodje kad se uspesno zavrsi nivo, i onda kad klikne opet na OK dodje do ovog bloka koda
            self.generateLetters() #pravim novi set slova, u toj metodi se takodje resetuje rec koju igrac pravi na prazno
            self.lblMinimumLetters.config(text=str(player.level)+". nivo: minimum reč od " + str(player.level + 2) + " slova",
                                  font="Helvetica 14 italic", bg="wheat3",
                                  fg="gray16")

            self.btn1_isactive = 1 #aktiviram sve dugmice posto sam ih prethodno deaktivirao
            self.btn2_isactive = 1
            self.btn3_isactive = 1
            self.btn4_isactive = 1
            self.btn5_isactive = 1
            self.btn6_isactive = 1
            self.btn7_isactive = 1
            self.btn8_isactive = 1
            self.btn9_isactive = 1
            self.btn10_isactive = 1
            self.btn11_isactive = 1
            self.btn12_isactive = 1

    def getRandom(self,list_count):
        r = random.randint(0, list_count)  # bira setove izmedju preostalih, kasnije se brise set koji je izabran, ne brisem ga odma da bi mogao da pristupim vrednostima
        return r

    def addLetter(self,letter,btn,numOfButton):
        if numOfButton is 1: #proveravam koje je dugme aktiviralo metodu da bih mogao da ga disablujem, parametre primam iz lambda funkcije u mouseclick eventu svakog dugmeta
            if self.btn1_isactive is 0:
                print("Button inactive.")#ako je dugme neaktivno (proveravam preko promenljive buduci da state="disabled" samo vizuelno disabluje dugme), ne unosi se slovo u rec
            else:
                self.word += letter #u suprotnom,ako je aktivno dugme dodajem slovo na promenljivu "self.word"
                self.lblWord.config(text=self.word) #prikazujem word promenljivu na ekranu
                btn.config(state="disabled") #disablujem dugme koje je kliknuto
                self.btn1_isactive=0 #rucno postavljam dugme na disablovano
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 2: #-||-
            if self.btn2_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn2_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 3:
            if self.btn3_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn3_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 4:
            if self.btn4_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn4_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 5:
            if self.btn5_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn5_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 6:
            if self.btn6_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn6_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 7:
            if self.btn7_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn7_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 8:
            if self.btn8_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn8_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 9:
            if self.btn9_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn9_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 10:
            if self.btn10_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn10_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 11:
            if self.btn11_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn11_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        elif numOfButton is 12:
            if self.btn12_isactive is 0:
                print("Button inactive.")
            else:
                self.word += letter
                self.lblWord.config(text=self.word)
                btn.config(state="disabled")
                self.btn12_isactive=0
                self.lblWord.config(fg="RoyalBlue3")
        else:
            print("Error adding letter/disabling button!")

    def addTime(self,event):
        if player.runThread!=0: #ako program NIJE u fazi u kojoj ne odbrojava sekunde nego se ceka korisnik da zapocne novi nivo, ne moze da se produzi vreme
            if(player.cash>=10):
                player.cash-=10
                self.lblBalance.config(text=str(player.cash)+"$", bg="Wheat3", fg="sea green", font="Helvetica 20 bold")
                player.seconds+=30
            else:
                messagebox.showerror("Ups!","Nemas dovoljno $ da produzis vreme!")
        else: #ako je program u fazi cekanja da korisnik zapocne novi nivo, ne moze da dodaje vreme
            print("Can't add time when game is in waiting phase!")

    def generateLetters(self):
        self.lblWord.config(text="") #svaki put kad se napravi novi nivo i kad se pozove ova metoda,text se vraca na prazno u labelu
        self.lblWord.grid(row=0, columnspan=6) #prikazana rec
        self.word="" #resetuje se rec svaki put kad se pozove ova metoda (kad se napravi novi nivo)
        self.lblMinimumLetters.grid(row=1, column=3,columnspan=3)
        player.lblTimeLeft.config(fg="wheat4")

        lblEmpty = Label(root, text="", height=2, bg="Wheat3")
        lblEmpty.grid(row=2, columnspan=6)#radi izgleda

        r = self.getRandom(len(player.list_of_sets)-1) #generisanje random broja seta slova,izmedju 1 i kolko ih je preostalo u listi svih setova slova

        btnLetter1 = Button(root, text=player.list_of_sets[r][0], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter1.grid(row=3, column=0)#buduci da bind-ovanje podrazumeva da se ne salju parametri u metodu vec se ona samo poziva(i to bez () ), pravim lambda funkciju i 3 parametra koji su mi potrebni za dodavanje slova na rec i disablovanje dugmeta
        btnLetter1.bind("<Button-1>",lambda event, letter=player.list_of_sets[r][0],btn=btnLetter1,numOfButton=1:self.addLetter(letter,btn,numOfButton)) #letter=dugme koje saljem u metodu za dodavanje slova, btn=saljem dugme u metodu kako bi ga tamo disablovo,numOfButton=saljem broj dugmeta jer disablovanje ne onemogucava da se opet unese isto slovo, samo vizuelno

        btnLetter2 = Button(root, text=player.list_of_sets[r][1], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter2.grid(row=3, column=1) #-||-
        btnLetter2.bind("<Button-1>", lambda event,letter=player.list_of_sets[r][1],btn=btnLetter2,numOfButton=2:self.addLetter(letter,btn,numOfButton))

        btnLetter3 = Button(root, text=player.list_of_sets[r][2], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter3.grid(row=3, column=2)
        btnLetter3.bind("<Button-1>",lambda event,letter=player.list_of_sets[r][2],btn=btnLetter3,numOfButton=3:self.addLetter(letter,btn,numOfButton))

        btnLetter4 = Button(root, text=player.list_of_sets[r][3], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter4.grid(row=3, column=3)
        btnLetter4.bind("<Button-1>",lambda event,letter=player.list_of_sets[r][3],btn=btnLetter4,numOfButton=4:self.addLetter(letter,btn,numOfButton))

        btnLetter5 = Button(root, text=player.list_of_sets[r][4], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter5.grid(row=3, column=4)
        btnLetter5.bind("<Button-1>",lambda event,letter=player.list_of_sets[r][4],btn=btnLetter5,numOfButton=5:self.addLetter(letter,btn,numOfButton))

        btnLetter6 = Button(root, text=player.list_of_sets[r][5], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter6.grid(row=3, column=5)
        btnLetter6.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][5],btn=btnLetter6,numOfButton=6:self.addLetter(letter,btn,numOfButton))

        lblEmpty_2 = Label(root, text="", height=1, bg="Wheat3")
        lblEmpty_2.grid(row=4, columnspan=6)#prazan prostor

        btnLetter7 = Button(root, text=player.list_of_sets[r][6], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter7.grid(row=5, column=0)
        btnLetter7.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][6],btn=btnLetter7,numOfButton=7:self.addLetter(letter,btn,numOfButton))

        btnLetter8 = Button(root, text=player.list_of_sets[r][7], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter8.grid(row=5, column=1)
        btnLetter8.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][7],btn=btnLetter8,numOfButton=8:self.addLetter(letter,btn,numOfButton))

        btnLetter9 = Button(root, text=player.list_of_sets[r][8], width=3, font="Helvetica 25 bold", bg="Wheat3",
                            fg="RoyalBlue3")
        btnLetter9.grid(row=5, column=2)
        btnLetter9.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][8],btn=btnLetter9,numOfButton=9:self.addLetter(letter,btn,numOfButton))

        btnLetter10 = Button(root, text=player.list_of_sets[r][9], width=3, font="Helvetica 25 bold", bg="Wheat3",
                             fg="RoyalBlue3")
        btnLetter10.grid(row=5, column=3)
        btnLetter10.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][9],btn=btnLetter10,numOfButton=10:self.addLetter(letter,btn,numOfButton))

        btnLetter11 = Button(root, text=player.list_of_sets[r][10], width=3, font="Helvetica 25 bold", bg="Wheat3",
                             fg="RoyalBlue3")
        btnLetter11.grid(row=5, column=4)
        btnLetter11.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][10],btn=btnLetter11,numOfButton=11:self.addLetter(letter,btn,numOfButton))

        btnLetter12 = Button(root, text=player.list_of_sets[r][11], width=3, font="Helvetica 25 bold", bg="Wheat3",
                             fg="RoyalBlue3")
        btnLetter12.grid(row=5, column=5)
        btnLetter12.bind("<Button-1>", lambda event, letter=player.list_of_sets[r][11],btn=btnLetter12,numOfButton=12:self.addLetter(letter,btn,numOfButton))

        lblEmpty_3 = Label(root, bg="Wheat3") #prazan prostor
        lblEmpty_3.grid(row=6, columnspan=6)


        self.lblBalance.grid(row=7, column=0)#label sa trenutnom kolicinom cash-a

        btnAddTime = Button(root, text="+00:30⏱ (10$)", bg="RoyalBlue3", fg="Wheat2", font="Helvetica 15")
        btnAddTime.grid(row=7, column=2, columnspan=2)#pomoc koja dodaje 30 sek na trenutno preostalo vreme
        btnAddTime.bind("<Button-1>",self.addTime)

        btnCheck = Button(root, text="❓", width=3, bg="Wheat3", fg="Wheat4", font="Helvetica 15 bold")
        btnCheck.grid(row=1, column=0)  # dugme za proveru da li postoji rec
        btnCheck.bind("<Button-1>", self.checkDictionary)

        btnClear = Button(root, text="✖", width=3, bg="Wheat3", fg="Wheat4", font="Helvetica 15 bold")
        btnClear.grid(row=1, column=1)  # dugme za brisanje cele reci
        btnClear.bind("<Button-1>",lambda event, btn1=btnLetter1, btn2=btnLetter2, btn3=btnLetter3,btn4=btnLetter4,btn5=btnLetter5,btn6=btnLetter6,btn7=btnLetter7,btn8=btnLetter8,btn9=btnLetter9,btn10=btnLetter10,btn11=btnLetter11,btn12=btnLetter12: self.clearWord(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12))

        btnOk = Button(root, text="✔", width=3, bg="Wheat3", fg="Wheat4", font="Helvetica 15 bold")
        btnOk.grid(row=1, column=2)  # dugme za potvrdu unete reci
        btnOk.bind("<Button-1>", self.submitWord)

        timer=TimerThread()
        timer.start()

        player.list_of_sets.remove(player.list_of_sets[r]) #brisanje random izabranog seta,kako se ne bi ponovio u nekom od sledecih nivoa

class TimerThread(threading.Thread):
    def run(self):
        player.runThread=1
        while player.seconds>-1 and player.runThread is 1: #broj sekundi se nalazi u klasi Player da bi mogao lakse da pristupim preko objekta
            if(player.seconds<1): #ako istekne vreme
                messagebox.showinfo("Isteklo vreme!","Nisi uspeo da upises rec na vreme!")
                game.lblWord.config(text="Nisi uspeo da upises rec na vreme. Da krenes ispocetka klikni ✔",fg="red") #text koji se prikazuje
                player.runThread=0 #zaustavlja se thread,kako kad bi kliknuo na dugme OK, ne bi pokusao da trazi rec u recniku nego da izbaci novi set slova
                player.seconds=60
                player.level=1 #vracanje na pocetak igre
                player.list_of_sets=[player.set_0, player.set_1, player.set_2, player.set_3,player.set_4,player.set_5,player.set_6,player.set_7,player.set_8,player.set_9,player.set_10,player.set_11,player.set_12,player.set_13,player.set_14,player.set_15,player.set_16,player.set_17,player.set_18,player.set_19]# punim listu sa svim setovima,jer su neki obrisani koji su bili izabrani
            try:
                if player.seconds<=5: #zadnji 5 sekundi boji u crveno
                    player.lblTimeLeft.config(fg="red")
                player.lblTimeLeft.config(text=str(player.seconds))

            except:
                print("Izlaz iz aplikacije") #exc se javi kad se ugasi app na X, jer thread pokusava da menja label koji ne postoji!!!
                exit(0)
            time.sleep(1)
            player.seconds-=1

class Player:
    def __init__(self):
        self.set_0 = ('t', 'a', 'o', 'i', 'a', 'e', 'z', 's', 't', 'r', 'p', 'i')
        self.set_1 = ('o', 'e', 'r', 't', 's', 'r', 'o', 'l', 'p', 'i', 'a', 'd')
        self.set_2 = ('u', 'p', 'r', 'd', 'a', 'o', 't', 'i', 's', 't', 'e', 's')
        self.set_3 = ('t', 'e', 'i', 't', 'a', 'r', 'u', 'p', 'o', 'a', 's', 'i')
        self.set_4 = ('u', 'g', 'o', 'a', 'i', 'e', 't', 's', 'r', 'o', 'i', 'n')
        self.set_5 = ('s', 't', 'e', 'p', 'i', 'd', 'z', 'i', 't', 'r', 'e', 'o')
        self.set_6 = ('p', 'u', 'i', 'r', 'o', 'g', 'i', 'o', 'd', 'a', 't', 's')
        self.set_7 = ('h', 'a', 'p', 'o', 'u', 'r', 's', 'a', 'r', 'g', 'i', 't')
        self.set_8 = ('u', 'z', 'o', 'a', 'e', 'i', 't', 'd', 'a', 'r', 'p', 'a')
        self.set_9 = ('a', 'e', 'd', 'a', 't', 'p', 'r', 'h', 'o', 'g', 'p', 'i')
        self.set_10 = ('i', 'e', 't', 'i', 's', 't', 'r', 'e', 'a', 's', 'z', 'd')
        self.set_11 = ('s', 't', 'e', 'p', 'a', 'u', 'r', 'a', 't', 'z', 'i', 'p')
        self.set_12 = ('t', 'p', 'a', 'r', 'u', 'a', 'd', 's', 'r', 'o', 'i', 'a')
        self.set_13 = ('r', 'a', 'i', 'p', 't', 'i', 'z', 'a', 'o', 't', 'd', 'a')
        self.set_14 = ('r', 'a', 'i', 't', 'o', 'r', 'd', 'i', 'a', 'n', 'a', 'p')
        self.set_15 = ('r', 'i', 'd', 'e', 'r', 'a', 's', 't', 'o', 'l', 'n', 'a')
        self.set_16 = ('i', 'e', 't', 'z', 'r', 'a', 'u', 'r', 'o', 't', 's', 'a')
        self.set_17 = ('v', 's', 'a', 'o', 'i', 'r', 'e', 'p', 't', 'a', 'd', 'b')
        self.set_18 = ('o', 'i', 't', 'o', 'e', 'r', 'm', 's', 'a', 'd', 'i', 'l')
        self.set_19 = ('p', 'o', 'i', 'k', 'm', 'n', 'u', 'r', 'p', 'i', 't', 'a')
        self.list_of_sets = [self.set_0, self.set_1, self.set_2, self.set_3,self.set_4,self.set_5,self.set_6,self.set_7,self.set_8,self.set_9,self.set_10,self.set_11,self.set_12,self.set_13,self.set_14,self.set_15,self.set_16,self.set_17,self.set_18,self.set_19]
        self.runThread=0
        self.cash=0
        self.level=1
        self.seconds=60
        self.lblTimeLeft = Label(root, text=str(self.seconds), bg="wheat3", fg="wheat4",
                                 font="Helvetica 20 bold")  # stavio sam kao atribut klase da bi mogao da pristupim i
        self.lblTimeLeft.grid(row=7, column=5)

root= Tk()
root.configure(background='Wheat3')
root.geometry("600x420")
root.resizable(False,False)
root.winfo_toplevel().title("Slozi rec!")

player=Player()

game = Game()
game.generateLetters()

root.mainloop()