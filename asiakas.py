def nayta_ui(): #Asiakkaan käyttöliittymä
    while True:
        print("Mitä haluat tehdä?")
        print("1. Listaa saatavilla olevat näytökset")
        print("2. Valitse näytös ja varaa paikka")
        print("3. Katso saatavilla olevat elokuvat")
        print("4. Poistu")


        Ui_input = input("Anna syöte: ")
        if Ui_input == "1":
            listaa_naytokset()
        elif Ui_input == "2":
            varaus()
        elif Ui_input == "3":
            listaa_naytokset_nimen_mukaan()
        elif Ui_input == "4":
            print("Näkemiin, Tervetuloa uudelleen!")
            break
    
def listaa_naytokset(): # Listaa leffat.csv kansiossa olevat näytökset  
    print()
    print("Teatterissa pyörivät näytökset:")
    with open("leffat.csv", "r") as tiedosto:
        elokuvat = tiedosto.readlines()
        for rivi in elokuvat: 
            osat = rivi.split(";")
            print(f"{osat[0]}, Kesto: {osat[1]} min, Sali nro: {osat[2]}, Vapaiden paikkojen määrä: {osat[3]}, Pvm: {osat[4]}, Kellonaika: {osat[5]}")
    print()

def listaa_naytokset_nimen_mukaan(): # Listaa leffat.csv kansiossa olevat näytökset nimen mukaan
    print()
    print("Teatterissa pyörivät näytökset:")
    lista_nimen_mukaan = []
    with open("leffat.csv", "r") as tiedosto:
        elokuvat = tiedosto.readlines()
        for rivi in elokuvat: 
            osat = rivi.split(";")
            if osat[0] not in lista_nimen_mukaan:
                lista_nimen_mukaan.append(osat[0])

        for osa in lista_nimen_mukaan:
            print(osa)
        
        print()
       
        jatka = input("Haluatko varata lipun? k/e: ")

        print()
        
        if jatka == "k":
            varaus()
        else:
            nayta_ui()
        
    
def varaus(): # Toteuttaa asiakkaan paikkavarauksen leffat.csv kansioon
    filename = "leffat.csv"

    with open(filename, "r") as tiedosto:
        elokuvat = tiedosto.readlines()

    laskuri = 1
    for rivi in elokuvat:
        osat = rivi.split(";")
        print(f"{laskuri}. {osat[0]}, Kesto: {osat[1]} min, Sali nro: {osat[2]}, Vapaiden paikkojen määrä: {osat[3]}, Pvm: {osat[4]}, Kellonaika: {osat[5]}")
        laskuri += 1

    print()
    valinta = int(input("Valitse näytös, syötä näytöksen numero: "))
    paikkojen_maara = int(input("Valitse paikkojen määrä: "))

    modified_content = []

    laskuri = 1
    for rivi in elokuvat:
        osat = rivi.split(";")
        if laskuri == valinta:
            if paikkojen_maara <= int(osat[3]):
                paikkavaraus = int(osat[3]) - paikkojen_maara
                osat[3] = str(paikkavaraus)
                rivi = ";".join(osat)
                print("Paikkojen varaus onnistui, Tervetuloa!")
            else:
                print("Paikkojen varaus epäonnistui")
        modified_content.append(rivi)
        laskuri += 1

    with open(filename, "w") as tiedosto:
        tiedosto.writelines(modified_content)

################## PÄÄOHJELMA ##################

nayta_ui() #avaa pääohjelman