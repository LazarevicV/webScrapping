from os.path import isfile
from abc import ABC, abstractmethod

from selenium import webdriver
import time 

from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("/usr/local/bin/chromedriver") 

#--------------------------------------------------------------------------------------------------------------
class Proizvod():

    #-----------privatna polja klase proizvod-----------
    __naziv_modela : str 
    __cena_modela : float 

    #-----------konstruktor klase Proizvod-----------
    def __init__(self, naziv_modela, cena_modela) -> None:
        self.__naziv_modela = naziv_modela
        self.__cena_modela = cena_modela

    #-----------geteri i seteri klase Proizvod-----------
    def get_naziv_modela(self):
        return self.__naziv_modela

    def get_cena(self):
        return self.__cena_modela

    def set_naziv_modela(self, novi_naziv_modela):
        self.__naziv_modela = novi_naziv_modela
    
    def set_cena(self, nova_cena_modela):
        self.__cena_modela = nova_cena_modela

    #-----------metode i funkcije klase Proizvod-----------
    @abstractmethod
    def konverzija_csv_objekat(self):
        pass 

    @staticmethod
    def sortiraj_po_nazivu(lista):
        lista.sort(key = lambda x: x.__naziv_modela)

    @staticmethod
    def sortiraj_po_ceni(lista):
        lista.sort(key = lambda x: x.__cena_modela, reverse=True)

    #-----------funkcija za konvertovanje u string-----------
    def __str__(self) -> str:
        return f'Naziv modela: {self.__naziv_modela}\nCena modela: {self.__cena_modela}\n'

#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
class StandardniMonitor(Proizvod):

    #-----------privatna polja klase StandardniMonitor-----------
    __naziv_vrsta_robe : str 
    __zemlja_proizvodnje : str 
    __boja : str 

    #-----------konstruktor klase StandardniMonitor-----------
    def __init__(self, naziv_modela, cena_modela, naziv_vrsta_robe, zemlja_porekla, boja) -> None:
        super().__init__(naziv_modela, cena_modela)
        self.__naziv_vrsta_robe = naziv_vrsta_robe
        self.__zemlja_proizvodnje = zemlja_porekla
        self.__boja = boja

    #-----------geteri i seteri klase StandardniMonitor-----------
    def get_naziv_vrsta_robe(self):
        return self.__naziv_vrsta_robe

    def get_zemlja_porekla(self):
        return self.__zemlja_proizvodnje

    def get_boja(self):
        return self.__boja

    def set_naziv_vrsta_robe(self, novi_naziv_vrsta_robe):
        self.__naziv_vrsta_robe = novi_naziv_vrsta_robe
    
    def set_zemlja_porekla(self, nova_zemlja_proizvodnje):
        self.__zemlja_proizvodnje = nova_zemlja_proizvodnje
    
    def set_boja(self, nova_boja):
        self.__boja = nova_boja

    #-----------metode i funkcije klase StandardniMonitor-----------
    @classmethod
    def dodatni_konstruktor(cls, csv_format):
        red = csv_format.strip()
        delovi_reda = red.split(',')
        naziv = delovi_reda[0]
        cena = float(delovi_reda[1])
        naziv_vrsta_robe = delovi_reda[2] 
        boja = delovi_reda[3]
        zemlja_porekla = delovi_reda[4]
        return cls(naziv, cena, naziv_vrsta_robe, boja, zemlja_porekla)

    @classmethod
    def konverzija_csv_objekat(cls, csv_format):
        trenutni_monitor = StandardniMonitor.dodatni_konstruktor(csv_format)
        return trenutni_monitor

    @staticmethod
    def ucitaj_iz_fajla(naziv_fajla):
        niz_monitora = []

        with open(naziv_fajla, 'r') as f:
            zaglavlje = f.readline()

            while True:
                trenutna_linija = f.readline()
                if trenutna_linija == '':
                    break 
                niz_monitora.append(StandardniMonitor.konverzija_csv_objekat(trenutna_linija))
        return niz_monitora

    @staticmethod 
    def upisi_u_fajl(lista_monitora, naziv_fajla):
        zaglavlje = 'Naziv,Cena,Naziv i vrsta robe,Boja,Zemlja Porekla\n'
        with open(naziv_fajla, 'w') as f:
            f.write(zaglavlje)
            for el in lista_monitora:
                trenutni_element = StandardniMonitor.konverzija_u_csv(el)
                f.write(trenutni_element)

    @staticmethod
    def cena_u_opsegu(lista_monitora, pocetna_cena, krajnja_cena):
        
        nova_lista_monitora = []

        for monitor in lista_monitora:
            if monitor.get_cena() >= pocetna_cena and monitor.get_cena() <= krajnja_cena:
                nova_lista_monitora.append(monitor)
        
        return nova_lista_monitora

    @classmethod
    def konverzija_u_csv(cls, gm1):
        return f'{gm1.get_naziv_modela()},{gm1.get_cena()},{gm1.get_naziv_vrsta_robe()},{gm1.get_zemlja_porekla()},{gm1.get_boja()}\n'

    #-----------funkcija za konvertovanje u string-----------
    def __str__(self) -> str:
        return super().__str__() + f'Naziv i vrsta robe: {self.__naziv_vrsta_robe}\nZemlja proizvodnje: {self.__zemlja_proizvodnje}\nBoja: {self.__boja}\n'
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
class GamingMonitor(Proizvod):
    #-----------privatna polja GamingMonitor klase-----------
    __dijagonala : str 
    __kontrast : str 
    __rezolucija : str 

    #-----------konstruktor GamingMonitor klase-----------
    def __init__(self, naziv_modela, cena_modela, dijagonala, kontrast, rezolucija) -> None:
        super().__init__(naziv_modela, cena_modela)
        self.__dijagonala = dijagonala 
        self.__kontrast = kontrast 
        self.__rezolucija = rezolucija

    #-----------geteri i seteri GamingMonitor klase-----------
    def get_dijagonala(self):
        return self.__dijagonala 
    
    def get_kontrast(self):
        return self.__kontrast

    def get_rezolucija(self):
        return self.__rezolucija

    def set_dijagonala(self, nova_dijagonala):
        if len(nova_dijagonala) < 3:
            print('Nova dijagonala ne zadovoljava odredjene parametre!')
            return 
        self.__dijagonala = nova_dijagonala

    def set_kontast(self, novi_kontrast):
        if len(novi_kontrast) < 3:
            print('Novi kontrast ne zadovoljava odredjene parametre!')
            return 
        self.__kontrast = novi_kontrast

    def set_rezolucija(self, nova_rezolucija):
        if len(nova_rezolucija) < 3:
            print('Nova rezolucija ne zadovoljava odredjene parametre!')
            return 
        self.__rezolucija = nova_rezolucija

    #-----------metode i funkcije GamingMonitor klase-----------
    @classmethod
    def dodatni_konstruktor(cls, csv_format):
        red = csv_format.strip()
        delovi_reda = red.split(',')
        naziv = delovi_reda[0]
        cena = float(delovi_reda[1])
        dijagonala = delovi_reda[2] 
        kontrast = delovi_reda[3]
        rezolucija = delovi_reda[4]
        return cls(naziv, cena, dijagonala, kontrast, rezolucija)

    @classmethod
    def konverzija_csv_objekat(cls, csv_format):
        trenutni_monitor = GamingMonitor.dodatni_konstruktor(csv_format)
        return trenutni_monitor

    @staticmethod
    def ucitaj_iz_fajla(naziv_fajla):
        niz_monitora = []

        with open(naziv_fajla, 'r') as f:
            zaglavlje = f.readline()

            while True:
                trenutna_linija = f.readline()
                if trenutna_linija == '':
                    break 
                niz_monitora.append(GamingMonitor.konverzija_csv_objekat(trenutna_linija))
        return niz_monitora

    @staticmethod 
    def upisi_u_fajl(lista_monitora, naziv_fajla):
        zaglavlje = 'Naziv,Cena,Dijagonala,Kontrast,Rezolucija\n'
        with open(naziv_fajla, 'w') as f:
            f.write(zaglavlje)
            for el in lista_monitora:
                trenutni_element = GamingMonitor.konverzija_u_csv(el)
                f.write(trenutni_element)

    @staticmethod
    def cena_u_opsegu(lista_monitora, pocetna_cena, krajnja_cena):
        
        nova_lista_monitora = []

        for monitor in lista_monitora:
            if monitor.get_cena() >= pocetna_cena and monitor.get_cena() <= krajnja_cena:
                nova_lista_monitora.append(monitor)
        
        return nova_lista_monitora

    @classmethod
    def konverzija_u_csv(cls, gm1):
        return f'{gm1.get_naziv_modela()},{gm1.get_cena()},{gm1.get_dijagonala()},{gm1.get_kontrast()},{gm1.get_rezolucija()}\n'

    #-----------funkcija za konvertovanje u string-----------
    def __str__(self) -> str:
        return super().__str__() + f'Dijagonala: {self.__dijagonala}\nKontrast: {self.__kontrast}\nRezolucija: {self.__rezolucija}\n'
#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------
class Tehnomanija:
    __web_driver : webdriver.Chrome

    def __init__(self, putanja = "/usr/local/bin/chromedriver") -> None:
        if not isfile(putanja):
            print(putanja, 'ne postoji!')
            return 
        self.__web_driver = webdriver.Chrome(putanja)

    def get_web_driver(self):
        return self.__web_driver

    def set_web_driver(self, novi_web_driver):
        if not isinstance(novi_web_driver, webdriver.Chrome):
            print('Web driver mora biti webdriver.Chrome!')
            return 
        self.__web_driver = novi_web_driver

    def idi_na_stranicu(self, putanja_stranice):
        try:
            self.__web_driver.get(putanja_stranice)
        except:
            print('Neuspelo obilazenje stranice!')
            return 

    def zatvori_browser(self):
        try:
            self.__web_driver.quit()
        except:
            print('Neuspelo zatvaranje browsera!')
            return

    def zatvori_tab_browsera(self):
        try:
            self.__web_driver.close()
        except:
            print('Neuspelo zatvaranje taba!')
            return 

    def sacekaj_impliticno(self, sekunde = 5):
        self.__web_driver.implicitly_wait(sekunde)

    def sve_putanje(self, broj_strana, pocetna_putanja, putanja_narednih='?currentPage='):

        lista_putanja = []
        if broj_strana == 0:
            return [pocetna_putanja]
        for i in range(broj_strana):
            putanja = f'{pocetna_putanja}{putanja_narednih}{i+1}'
            lista_putanja.append(putanja)
        return lista_putanja
    
    # postavljam defaultne vrednosti na prazan string, i onda kada pri
    # pozivu funkcije dodelim neku vrednost odgovarajucem nazivom
    def trazi_element(self, element_id = '', element_class = '', element_tag_name = '', element_name = '', element_link_text = '', element_partial_text = '', element_css_selector = ''):

        if element_id != '':
            try:
                rez = self.__web_driver.find_element(By.ID, element_id) #find_element -> jedan element zbog id-a
                return rez #vrati sta smo nasli 
            except:
                return None # ili vrati None 
                # ako trazimo preko id-a on je jedinstven, vraticu ili rez ili None, u zavisnosti od toga da li je uspeo try blok 

        if element_class != '':
            try:
                rez = self.__web_driver.find_elements(By.CLASS_NAME, element_class)
                return rez 
            except: 
                return [] 
                # svuda ostalo vracam ili rez ili []

        if element_tag_name != '':
            try:
                rez = self.__web_driver.find_elements(By.TAG_NAME, element_tag_name)
                return rez 
            except:
                return []

        if element_name != '':
            try:
                rez = self.__web_driver.find_elements(By.NAME, element_name)
                return rez 
            except:
                return []

        if element_css_selector != '':
            try:
                rez = self.__web_driver.find_elements(By.CSS_SELECTOR, element_css_selector)
                return rez 
            except:
                return []

        if element_partial_text != '':
            try:
                rez = self.__web_driver.find_elements(By.PARTIAL_LINK_TEXT, element_partial_text)
                return rez 
            except:
                return []

        if element_link_text != '':
            try:
                rez = self.__web_driver.find_elements(By.LINK_TEXT, element_link_text)
                return rez 
            except:
                return []
        
    def sacekaj(self, sekunde = 5):
        time.sleep(sekunde)

    def vrati_se_nazad(self):
        self.__web_driver.back()

    def skroluj_na_dno_strane(self):
        self.__web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def izracunaj_broj_strana(self, putanja):
        print('Brojanje stranica...')
        self.idi_na_stranicu(putanja)

        poslednja_strana = self.trazi_element(element_class='end')

        if len(poslednja_strana) == 0:
            return 0

        broj_strana = int(poslednja_strana[0].get_attribute('href').split('=',2)[1])
        print('Broj strana:',broj_strana+1)

        return broj_strana

    def obidji_stranicu(self, putanja, naziv_fajla, tip_objekta, element_id='', element_class='', element_tag_name='', element_name='', element_link_text='', element_partial_text='', element_css_selector=''):

        linkovi_proizvoda = []
        print(putanja)

        self.idi_na_stranicu(putanja)

        svi_proizvodi = self.trazi_element(element_id, element_class, element_tag_name, element_name, element_link_text, element_partial_text, element_css_selector)

        self.sacekaj_impliticno(5)

        for p in svi_proizvodi:
            linkovi_proizvoda.append(p.get_attribute('href'))

        f = open(naziv_fajla, 'a')

        for link in linkovi_proizvoda:
            self.idi_na_stranicu(link)
            objekat = self.dohvati_podatke(tip_objekta)

            print(objekat)
            if objekat != None:
                if tip_objekta == 'gaming':
                    print('Jeste gaming monitor')
                    f.write(GamingMonitor.konverzija_u_csv(objekat))
                    
                else:
                    print('Standardni monitor')
                    f.write(StandardniMonitor.konverzija_u_csv(objekat))
        f.close()

    def dohvati_podatke(self, tip_objekta):
        try:
            naziv_proizvoda = self.trazi_element(element_css_selector='h1')[0].text.replace(',','')
            print(naziv_proizvoda)
            puna_cena = self.trazi_element(element_class='product-price-newprice')[0].text 

            cena = puna_cena.split(' ', 1)[0].replace('.','')
            print(cena)
            self.skroluj_na_dno_strane()
            self.sacekaj(3)
            self.skroluj_na_dno_strane()

            atributi = self.trazi_element(element_class='feature-name')
            vrednosti = self.trazi_element(element_class='feature-value')

            imena_atributa = []
            vrednosti_atributa = []

            duzina = len(atributi)

            for i in range(duzina):
                imena_atributa.append(atributi[i].text)
                vrednosti_atributa.append(vrednosti[i].text)

            # for i in range(duzina):
            #     print(imena_atributa[i],vrednosti_atributa[i])

            if tip_objekta == 'gaming':
                try:
                    brojac1 = 0
                    for i in range(duzina):
                        if imena_atributa[i] == 'Dijagonala':
                            brojac1 = i
                    print(vrednosti_atributa[brojac1])
                    dijagonala = vrednosti_atributa[brojac1].replace(',','')

                    brojac2 = 0
                    for i in range(duzina):
                        if imena_atributa[i] == 'Kontrast':
                            brojac2 = i
                    print(vrednosti_atributa[brojac2])
                    kontrast = vrednosti_atributa[brojac2].replace(',','')

                    brojac3 = 0
                    for i in range(duzina):
                        if imena_atributa[i] == 'Rezolucija':
                            brojac3 = i
                    print(vrednosti_atributa[brojac3])
                    rezolucija = vrednosti_atributa[brojac3].replace(',','')

                    return GamingMonitor(naziv_proizvoda, cena, dijagonala, kontrast, rezolucija)
                except:
                    return None
            else:
                naziv_vrsta_robeIndex = imena_atributa.index('Naziv i vrsta robe')
                zemlja_proizvodnjeIndex = imena_atributa.index('Zemlja proizvodnje')
                bojaIndex = imena_atributa.index('Boja')

                naziv_vrsta_robe = vrednosti_atributa[naziv_vrsta_robeIndex].replace(',','')
                zemlja_proizvodnje = vrednosti_atributa[zemlja_proizvodnjeIndex].replace(',','')
                boja = vrednosti_atributa[bojaIndex].replace(',','')

                return StandardniMonitor(naziv_proizvoda, cena, naziv_vrsta_robe, zemlja_proizvodnje, boja)
        except:
            print('Ne radi dohvati podatke')
            pass

    def prodji_sve_stranice(self, sve_putanje, putanja_do_fajla, tip_objekta, element_id='', element_class='', element_tag_name='', element_name='', element_link_text='', element_partial_text='', element_css_selector=''):
        print('Prolazak kroz sve stranice...')

        index = 0
        for putanja in sve_putanje:
            index += 1
            print('Trenutna stranica:',index)
            self.obidji_stranicu(putanja, putanja_do_fajla, tip_objekta, element_id, element_class, element_tag_name, element_name, element_link_text, element_partial_text, element_css_selector)

            self.sacekaj_impliticno(5)

        print('Prolazak zavrsen!')


def main():

    t1 = Tehnomanija()

    #standardni monitor
    standardniMonitorPutanja = 'https://www.tehnomanija.rs/c/kompjuteri-hardware-i-kancelarijska-oprema/monitori/standardni-monitori-10030502'

    broj_strana_sm = t1.izracunaj_broj_strana(standardniMonitorPutanja)
    putanje_strana_sm = t1.sve_putanje(broj_strana_sm, standardniMonitorPutanja)

    putanje_strana_sm.insert(0, standardniMonitorPutanja)

    f = open('standardni-monitor.csv', 'w')
    zagljavlje_obicne = 'Naziv,Cena,Naziv i vrsta robe,Zemlja proizvodjnje,Boja\n'
    f.write(zagljavlje_obicne)
    f.close()

    t1.prodji_sve_stranice(putanje_strana_sm, 'standardni-monitor.csv', 'Standardni', element_class='product-carousel--href')

    standardni_monitori = StandardniMonitor.ucitaj_iz_fajla('standardni-monitor.csv')
    StandardniMonitor.sortiraj_po_ceni(standardni_monitori)

    StandardniMonitor.upisi_u_fajl(standardni_monitori, 'standardni-sortirani-cena.csv')

    # gaming monitor
    gamingMonitorPutanja = 'https://www.tehnomanija.rs/c/kompjuteri-hardware-i-kancelarijska-oprema/monitori/gaming-monitori-10030501'

    broj_strana_gm = t1.izracunaj_broj_strana(gamingMonitorPutanja)
    putanje_strane_gm = t1.sve_putanje(broj_strana_gm, gamingMonitorPutanja)

    zaglavlje_gejming = 'Naziv,Cena,Dijagonala,Kontrast,Rezolucija\n'

    f = open('gaming-monitor.csv', 'w')
    f.write(zaglavlje_gejming)
    f.close()

    t1.prodji_sve_stranice(putanje_strane_gm, 'gaming-monitor.csv', 'gaming', element_class='product-carousel--href')

    gaming_monitori = GamingMonitor.ucitaj_iz_fajla('gaming-monitor.csv')
    GamingMonitor.sortiraj_po_ceni(gaming_monitori)

    GamingMonitor.upisi_u_fajl(gaming_monitori, 'gaming-sortirani-cena.csv')

if __name__ == '__main__':
    main()