-----------------OPIS------------------
-Mini desktop igrica koja testira logiku i vestinu sklapanja reci.
-Zadatak igraca je da za dato vreme osmisli rec dovoljne duzine za prolaz.
-Potrebna duzina reci se svakim nivoom povecava, tako da igrac kako napreduje
kroz nivoe mora svaki put da smisli duzu rec od prethodne.
-Igrica ima 6 nivoa:
	1. nivo = rec od minimum 3 slova
	2. nivo = rec od minimum 4 slova
	3. nivo = rec od minimum 5 slova
	4. nivo = rec od minimum 6 slova
	5. nivo = rec od minimum 7 slova
	6. nivo = rec od minimum 8 slova
-Za svaku rec koju igrac sklopi, osvaja $ u zavisnosti od duzine reci
-Igrac moze da trosi $ na produzavanje vremena ukoliko mu je potrebno



-----------------UPUTSTVO------------------
-Klikom na slova koja se prikazu na ekranu, slovo po slovo se sklapa rec
-Postoje 4 opcije dostupne igracu:
	DUGME |?| - boji rec:
					  zeleno -> ako postoji u recniku
					  narandzasto -> ako postoji u recniku ali nije dovoljno dugacka za prolaz
					  crveno -> ako rec ne postoji u recniku
					  
	DUGME |X| - brise celu rec
	
	DUGME |✔| - potvrdjuje sklopljenu rec
	
	DUGME |+00:30| - produzava vreme za 30sekundi, za cenu $

-U svakom nivou tajmer otkucava 60 sekundi (ukoliko igrac ne produzi vreme)


-----------------NAPOMENE------------------
-Rec koju igrac sklopi proverava se u recnicima koji su u .txt formatu i nalaze se u folderu projekta
-Recnik u elektronskom formatu sam nasao na internetu, sto podrazumeva da dosta reci fali
-Recnik sam u c# podelio na 12 txt fajlova prema duzini reci,kako ne bi svaki put pri proveri reci pretrazivao ceo recnik sa svim recima,
vec samo sa onom duzinom reci koju je igrac sklopio (npr ako igrac sklopi rec od 6 slova,ta rec se pretrazuje u recnik_6.txt fajlu koji sadrzi sve reci sa 6 slova)
-Kombinacije slova sam zadao sam kako bi u svakom nivou moglo da se sklopi dovoljno dugacka rec
-Kombinacije slova idu random svaki put, trenutno ih ima 20 
-Nisam puno obracao paznju na konvencije imenovanja promenljivih,metoda,klasa itd
-GUI je napravljen preko Tkinter-a



-----------------CREDITS------------------
Goran Rakic, za recnik u elektronskom formatu koji sam iskoristio
https://github.com/grakic/hunspell-sr/blob/master/sr-Latn.dic


