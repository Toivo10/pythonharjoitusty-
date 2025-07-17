def nayta_ui(): # Käyttöliittymä
    while True:
        print("Mitä haluat tehdä?")
        print("1. Lisää näytös")
        print("2. Poista näytös")
        print("3. Listaa olemassa olevat näytökset")
        print("4. Sulje ohjelma")
        

        Ui_input = input("Anna syöte: ")
        if Ui_input == "1":
            lisaa_naytos()
        elif Ui_input == "2":
            poista_naytos()
        elif Ui_input == "3":
            listaa_naytokset()
        elif Ui_input == "4":
            lajittele_naytokset()
            print("Näkemiin!")
            break


def lisaa_naytos(): # Elokuvan lisääminen leffat.csv tiedostoon
    while True:
        elokuva_naytos = {}

        elokuva_naytos['elokuva'] = input("Anna elokuvan nimi: ")
        elokuva_naytos['kesto'] = input("Anna kesto(min): ")
        elokuva_naytos['sali_numero'] = input("Anna salin numero: ")
        elokuva_naytos['vapaat_paikat'] = input("Anna vapaiden paikkojen määrä: ")
        elokuva_naytos['paivamaara'] = input("Anna päivämäärä (muodossa DD-MM-YYYY): ")
        elokuva_naytos['aika'] = input("Anna kellonaika (muodossa HH:MM): ")

        with open("leffat.csv", 'a') as tiedosto:
            # Muodostetaan merkkijono manuaalisesti
            elokuvanaytos_rivi = f"{elokuva_naytos['elokuva']};{elokuva_naytos['kesto']};{elokuva_naytos['sali_numero']};{elokuva_naytos['vapaat_paikat']};{elokuva_naytos['paivamaara']};{elokuva_naytos['aika']}\n"
            tiedosto.write(elokuvanaytos_rivi)
        print()
        print("Näytös lisätty!")
        jatka = input("Haluatko lisätä uuden näytöksen? k/e: ")
        if jatka != "k":
            break
    print()


def poista_naytos():
    while True:
        with open("leffat.csv", "r") as tiedosto:
            naytokset = tiedosto.readlines()

        print()
        print("Näytökset:")
        for rivi in naytokset:
            print(rivi.strip())  # Tulostetaan näytökset
        print()

        elokuvan_nimi = input("Anna elokuvan nimi: ")
        paivamaara = input("Anna päivämäärä (muodossa DD-MM-YYYY): ")
        aika = input("Anna kellonaika (muodossa HH:MM): ")

        loydetty = False

        with open("leffat.csv", 'w') as tiedosto:
            for rivi in naytokset:
                elokuvanaytos_tiedot = rivi.strip().split(';')
                if (
                    elokuvanaytos_tiedot[0] == elokuvan_nimi and
                    elokuvanaytos_tiedot[4] == paivamaara and
                    elokuvanaytos_tiedot[5] == aika
                ):
                    loydetty = True
                else:
                    tiedosto.write(rivi)

        if loydetty:
            print("Näytös poistettu onnistuneesti.")
        else:
            print("Näytöstä ei löytynyt annetuilla tiedoilla.")

        jatka = input("Haluatko poistaa toisen Näytöksen? k/e: ")
        if jatka != "k":
            break

    print()

def listaa_naytokset(): # leffat.csv kansiossa olevien näytösten printtaus
    print()
    print("Ohjelmassa pyörivät näytökset:")
    with open("leffat.csv", "r") as tiedosto: # Luetaan tiedosto listaan
        elokuvat = tiedosto.readlines()
        for rivi in elokuvat: 
            print(rivi.strip()) # tulostetaan elokuvat
    print()

def naytosten_lajittelu(rivi):
    pvm, aika = rivi.split(";")[4], rivi.split(";")[5]
    pvm_osa = list(map(int, pvm.split("-")))
    aika_osa = list(map(int, aika.split(":")))
    return (pvm_osa, aika_osa)

def lajittele_naytokset():
    with open("leffat.csv", "r") as file:
        rivit = file.readlines()

    rivit.sort(key=naytosten_lajittelu)

    with open("leffat.csv", "w") as file:
        file.writelines(rivit)


################## PÄÄOHJELMA ##################

nayta_ui() #avaa pääohjelman
