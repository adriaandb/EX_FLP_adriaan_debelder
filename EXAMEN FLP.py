import mod_vertalers as mv

lijst_antw=mv.de_vertalers_antwerpen
lijst_lim=mv.de_vertalers_limburg

#---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
#Toon alle vertalers van je regio

def toon_tolken(lijst):
    print("-------------------------------")
    print("alle vertalers van je regio:")
    for key, value in lijst.items():
            print("Naam: " + key + "',Moedertaal: " + lijst[key]["moedertaal"] + ", Beschikbaar: " + lijst[key][
                "beschikbaar"])
            for x in value:
                # print(value[x])
                if x == "talen":
                    # print(value[x])
                    for y in value[x]:
                        print(y)
# ---------------------------------------------------------------------------
#Toon beschikbare vertalers van je regio

def toon_tolken_vrij(lijst):
    print("-------------------------------")
    print("beschikbare vertalers van je regio:")
    for key, value in lijst.items():
        if lijst[key]["beschikbaar"] == "ja":
            print("Naam: " + key + "',Moedertaal: " + lijst[key]["moedertaal"] + ", Beschikbaar: " + lijst[key][
                "beschikbaar"])
            for x in value:
                # print(value[x])
                if x == "talen":
                    # print(value[x])
                    for y in value[x]:
                        print(y)

# ---------------------------------------------------------------------------
#Toon beschikbare vertalers van je regio, plus de talen die ze geven

def toon_tolk_taal(lijst):
    print("-------------------------------")
    print("beschikbare vertalers van je regio, plus de talen die ze geven:")
    for key, value in lijst.items():
        if lijst[key]["beschikbaar"] == "ja":
            print("Naam: "+key+"',Moedertaal: "+lijst[key]["moedertaal"]+", Beschikbaar: "+lijst[key]["beschikbaar"])
            for x in value:
                #print(value[x])
                if x=="talen":
                    #print(value[x])
                    for y in value[x]:
                        print(y)



# ---------------------------------------------------------------------------
#Voeg een vertaler toe

def add_tolk(lijst):
    print("-------------------------------")
    print("Voeg een vertaler toe:")
    naam=input("wat is de naam:")
    moedertaal=input("wat is de moedertaal:")


    nieuwe_tolk={ naam: {"moedertaal" : moedertaal, "talen":[] , "beschikbaar" : ""}}


    wachtwoord="wachtwoord"
    wachtwoordklant=input("geef het wachtwoord in:")
    if wachtwoordklant==wachtwoord:
        lijst.update(nieuwe_tolk)
        print("tolk is toegevoegd")

    return lijst
# ---------------------------------------------------------------------------
#Verwijder een vertaler

def del_tolk(lijst):
    print("-------------------------------")
    print("Verwijder een vertaler:")

    bekend = ""
    while not bekend == "j":
        naamtolk = input("Geef naam in van te verwijderen vertaler")
        for x in lijst:
            if naamtolk == x:
                bekend = "j"
        else:
            if not bekend == "j":
                print("Vertaler niet bekend")


    wachtwoord = "wachtwoord"
    wachtwoordklant = input("geef het wachtwoord in:")
    if wachtwoordklant == wachtwoord:
        lijst.pop(naamtolk)
        print("tolk '"+naamtolk+"' is verwijderd")


# ---------------------------------------------------------------------------
#Voeg taal toe aan vertaler

def add_taal(lijst):
    print("-------------------------------")
    print("Voeg taal toe aan vertaler:")

# ---------------------------------------------------------------------------
#Reserveer een vertaler

def res_tolk(lijst):
    print("-------------------------------")
    print("Reserveer een vertaler:")

# ---------------------------------------------------------------------------
#Toon lijst van vertalers met moedertaal naar keuze

def toon_moedertaal(lijst):
    print("-------------------------------")
    print("lijst van vertalers met moedertaal naar keuze:")

# ---------------------------------------------------------------------------

def menu():

    print("1. Toon alle vertalers van je regio")
    print("2. Toon beschikbare vertalers van je regio")
    print("3. Toon beschikbare vertalers van je regio, plus de talen die ze geven")
    print("4. Voeg een vertaler toe")
    print("5. Verwijder een vertaler")
    print("6. Voeg taal toe aan vertaler")
    print("7. Reserveer een vertaler")
    print("8. Toon lijst van vertalers met moedertaal naar keuze")

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------

#Hoofdprogramma:
lijst=[]
print("Welkom bij 'De Vertalers'!")
print("Van waar ben je:")
print("1. Antwerpen")
print("2. Limburg")
keuze=input("Maak je keuze:")
if keuze=="1":
    lijst=lijst_antw
elif keuze=="2":
    lijst=lijst_lim
print("je koos", keuze)
menukeuze=""


while True:
    print("-------------------------------")
    menu()
    menukeuze = input("Maak je keuze (of typ 'stop':)")
    print("-------------------------------")

    if menukeuze == "1":
        print("je koos", menukeuze)
        toon_tolken(lijst)
    elif menukeuze == "2":
        toon_tolken_vrij(lijst)
    elif menukeuze == "3":
        toon_tolk_taal(lijst)
    elif menukeuze == "4":
        add_tolk(lijst)
    elif menukeuze == "5":
        del_tolk(lijst)
    elif menukeuze == "6":
        add_taal(lijst)
    elif menukeuze == "7":
        res_tolk(lijst)
    elif menukeuze == "8":
        toon_moedertaal(lijst)
    elif menukeuze == "stop":
        break
