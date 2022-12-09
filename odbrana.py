from os.path import isfile 

from time import sleep 

from selenium import webdriver
from selenium.webdriver.common.by import By

class PripremaZaIspit:

    __naziv_predmeta : str 
    __cena : float 

    def __init__(self, naziv_predmeta, cena) -> None:
        self.__naziv_predmeta = naziv_predmeta
        self.__cena = cena 

    def get_naziv_predmeta(self):
        return self.__naziv_predmeta
    
    def get_cena(self):
        return self.__cena
    
    def set_naziv_predmeta(self, novi_naziv):
        if len(novi_naziv) < 2:
            print('Novi naziv predmeta mora imati barem 2 karaktera!')
            return 
        self.__naziv_predmeta = novi_naziv

    def set_cena(self, nova_cena):
        if nova_cena < 0:
            print('Nova cena mora biti pozitivna vrednost!')
            return 
        self.__cena = nova_cena

    @classmethod
    def konverzija_u_csv(cls, objekat):
        return f'{objekat.get_naziv_predmeta()},{objekat.get_cena()}\n'

    @staticmethod
    def upisi_u_fajl(lista_objekata, naziv_fajla):
        zaglavlje = 'Naziv predmeta,Cena\n'
        with open(naziv_fajla, 'w') as f:
            f.write(zaglavlje)
            for o in lista_objekata:
                trenutni_objekat = (PripremaZaIspit.konverzija_u_csv(o))
                f.write(trenutni_objekat)

    def __str__(self) -> str:
        return f'Naziv predmeta: {self.__naziv_predmeta}\nCena: {self.__cena}\n'

class Raf:

    __driver : webdriver.Chrome
    
    def __init__(self, putanja_drajver = '/usr/local/bin/chromedriver') -> None:
        self.__driver = webdriver.Chrome(putanja_drajver)

    def get_drajver(self):
        return self.__driver

    def set_drajver(self, novi_veb_drajver):
        if not isinstance(novi_veb_drajver, webdriver.Chrome):
            print('webdriver mora biti webdriver.Chrome!')
            return 
        self.__driver = novi_veb_drajver
    
    def idi_na_stranicu(self, putanja_stranice):
        try:
            self.__driver.get(putanja_stranice)
        except:
            print('Neuspelo obilazenje stranice!')
            return 

    def zatvori_browser(self):
        try:
            self.__driver.quit()
        except:
            print('Neuspelo zatvaranje chroma!')
            return 
    
    def zatvori_tab(self):
        try:
            self.__driver.close()
        except:
            print('Neuspelo zatvaranje browsera!')
            return 

    def sacekaj_implicitno(self, vreme = 5):
        self.__driver.implicitly_wait(vreme)

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

    def dobi_link_dokumenta(self, putanja, naziv_fajla):

        linkovi_proizvoda = []
        print(putanja)

        self.idi_na_stranicu(putanja)

        for a in self.__driver.find_elements(By.CLASS_NAME, 'button-outline'):
            link = a.get_attribute('href')
            linkovi_proizvoda.append(link)
            print(link)

        pravi_link = linkovi_proizvoda[0]

        return pravi_link

    def pokupi_vrednosti_iz_dokumenta(self, putanja):

        self.__driver.get(putanja)
        informacije = self.__driver.find_element(By.CLASS_NAME, 'cBGGJ')

        tekst = informacije.text

        sredjen_tekst = tekst.strip()
        print(sredjen_tekst)
        print(type(sredjen_tekst))

        podeli_na_redove = sredjen_tekst.split('\n')

        print(podeli_na_redove)

        indexStudija = podeli_na_redove.index('- Strukovne studije:')
        print(indexStudija)
        prva_priprema = podeli_na_redove[11]
        druga_priprema = podeli_na_redove[12]
        print(prva_priprema, druga_priprema)

        prva_priprema = prva_priprema.split(' ')
        druga_priprema = druga_priprema.split(' ')

        naziv_pripreme1 = f'{prva_priprema[0]} {prva_priprema[1]} {prva_priprema[2]} {prva_priprema[3]}'

        cena_pripreme1 = int(prva_priprema[4])

        naziv_pripreme2 = f'{druga_priprema[0]} {druga_priprema[1]} {druga_priprema[2]} {druga_priprema[3]}'

        cena_pripreme2 = int(druga_priprema[4])

        prva_priprema_objekat = PripremaZaIspit(naziv_pripreme1, cena_pripreme1)
        druga_priprema_objekat = PripremaZaIspit(naziv_pripreme2, cena_pripreme2)

        lista_priprema = [prva_priprema_objekat, druga_priprema_objekat]

        PripremaZaIspit.upisi_u_fajl(lista_priprema, 'podaci.csv')

def main():
    
    r1 = Raf()

    link_dokumenta = r1.dobi_link_dokumenta('https://raf.edu.rs/', 'podaci.csv')
    r1.pokupi_vrednosti_iz_dokumenta(link_dokumenta)

    r1.zatvori_browser()


if __name__ == '__main__':
    main()