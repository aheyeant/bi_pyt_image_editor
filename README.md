    Výstupem semestrální práce bude GUI-aplikace napsaná v Python'u, která dokáže načíst vstupní obrázek a na něm provádět vybrané základní grafické operace (následující operace jsou vyžadovány, ale zájemci si mohou seznam libovolně rozšířit):

	převrácení obrazu libovolným směrem (o násobky 90 °);
	zrcadlení;
	inverzní obraz;
	převod do odstínů šedi;
	zesvětlení/ztmavení;
	zvýraznění hran (rozumí se samozřejmě v obraze).

	Přitom na načtení (a případné uložení) obrázků můžete použít (ale nemusíte) metody knihovny Pillow, na zpracování operací však nikoli! Všechny operace budou napsané „ručně“ pomocí čistého Pythonu a Numpy (plus případné optimalizace pomocí Numby či Cythonu), abyste se je naučili používat. (Samozřejmě že jsou už dávno x-krát naprogramované v několika dalších dostupných knihovnách, a to optimalizovaně a rychle, ale to by samozřejmě nemělo jako semestrálka vůbec žádný smysl.)

	Co se aplikace týká, může to být buď klasické GUI (tkinter není podmínkou, klidně si to pište ve wx nebo třeba i v Qtéčku) nebo webové GUI, kde server poběží v Python'u. V obou případech očekávám u prováděných operací vizuální odezvu nad zpracovávaným obrázkem
